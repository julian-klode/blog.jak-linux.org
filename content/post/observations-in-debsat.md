---
title: "Observations in Debian dependency solving"
date: 2024-05-24T10:57:00+02:00
---

In my previous blog, I explored [The New APT 3.0 solver](https://blog.jak-linux.org/2024/05/14/solver3/).
Since then I have been at work in the test suite making tests pass and fixing some bugs.

You see for all intents and purposes, the new solver is a very stupid naive DPLL SAT solver (it just
so happens we don't actually have any pure literals in there). We can control it in a bunch of ways:

1. We can mark packages as "install" or "reject"
2. We can order actions/clauses. When backtracking the action that came later will be the first we
   try to backtrack on
3. We can order the choices of a dependency - we try them left to right.

This is about all that we really want to do, we can't go if we reach a conflict, say "oh but this
conflict was introduced by that upgrade, and it seems more important, so let's not backtrack on
the upgrade request but on this dependency instead.".

This forces us to think about lowering the dependency problem into this form, such that not only
do we get formally correct solutions, but also semantically correct ones. This is nice because
we can apply a systematic way to approach the issue rather than introducing ad-hoc rules in the
old solver which had a "which of these packages should I flip the opposite way to break the conflict"
kind of thinking.

Now our test suite has a whole bunch of these semantics encoded in it, and I'm going to share some
problems and ideas for how to solve them. I can't wait to fix these and the error reporting and
then turn it on in Ubuntu and later Debian (the defaults change is a post-trixie change, let's
be honest).

## `apt upgrade` is hard

The `apt upgrade` commands implements a safe version of dist-upgrade that essentially calculates the
dist-upgrade, and then undoes anything that would cause a package to be removed, but it (unlike its
`apt-get` counterpart) allows the solver to install new packages.

Now, consider the following package is installed:

    X Depends: A (= 1) | B

An upgrade from `A=1` to `A=2` is available. What should happen?

The classic solver would choose to remove `X` in a dist-upgrade, and then upgrade `A`, so it's answer
is quite clear: Keep back the upgrade of `A`.

The new solver however sees two possible solutions:

1. Install `X` to satisfy `X Depends A (= 1) | B`.
2. Keep back the upgrade of `A`

Which one does it pick? This depends on the order in which it sees the upgrade action for A and the
dependency, as it will backjump chronologically. So

1. If it gets to the dependency first, it marks `A=1` for install to satisfy `A (= 1)`. Then it gets
   to the upgrade request, which is just `A Depends A (= 2) | A (= 1)` and sees it is satisfied
   already and is content.

2. If it gets to the upgrade request first, it marks `A=2` for install to satisfy `A (= 2)`. Then
   later it gets to `X Depends: A (= 1) | B`, sees that `A (= 1)` is not satisfiable, and picks `B`.

We have two ways to approach this issue:

1. We always order upgrade requests last, so they will be kept back in case of conflicting dependencies
2. We require that, for `apt upgrade` a currently satisfied dependency must be satisfied by currently installed
   packages, hence eliminating `B` as a choice.

## Recommends are hard too

See if you have a `X Recommends: A (= 1)` and a new version of `A`, `A (= 2)`, the solver currently
will silently break the `Recommends` in some cases.

But let's explore what the behavior of a `X Recommends: A (= 1)` in combination with an available upgrade
of `A (= 2)` should be. We could say the rule should be:

- An `upgrade` should keep back `A` instead of breaking the `Recommends`
- A `dist-upgrade` should either keep back `A` or remove `X` (if it is obsolete)

This essentially leaves us the same choices as for the previous problem, but with an interesting twist.
We can change the ordering (and we already did), but we could also introduce a new rule, "promotions":

> A Recommends in an installed package, or an upgrade to that installed package, where the Recommends
> existed in the installed version, that is currently satisfied, must continue to be satisfied, that is,
> it effectively is promoted to a Depends.

This neatly solves the problem for us. We will never break Recommends that are satisfied.

Likewise, we already have a Recommends demotion rule:

> A Recommends in an installed package, or an upgrade to that installed package, where the Recommends
> existed in the installed version, that is currently unsatisfied, will not be further evaluated (it
> is treated like a Suggests is in the default configuration).

Whether we should be allowed to break Suggests with our decisions or not (the old autoremover did not,
for instance) is a different decision. Should we promote currently satisified Suggests to Depends as well?
Should we follow currently satisified Suggests so the solver sees them and doesn't autoremove them,
but treat them as optional?

## tightening of versioned dependencies

Another case of versioned dependencies with alternatives that has complex behavior is something like

    X Depends: A (>= 2) | B
    X Recommends: A (>= 2) | B

In both cases, installing `X` should upgrade an `A < 2` in favour of installing `B`. But a naive
SAT solver might not. If your request to keep A installed is encoded as `A (= 1) | A (= 2)`, then
it first picks `A (= 1)`. When it sees the Depends/Recommends it will switch to `B`.

We can solve this again as in the previous example by ordering the "keep A installed" requests after
any dependencies. Notably, we will enqueue the common dependencies of all A versions first before
selecting a version of A, so something may select a version for us.


## version narrowing instead of version choosing

A different approach to dealing with the issue of version selection is to not select a version
until the very last moment. So instead of selecting a version to satisfy `A (>= 2)` we instead
translate

    Depends: A (>= 2)

into two rules:

1. The package selection rule:

        Depends: A

    This ensures that any version of `A` is installed (i.e. it adds a version choice clause, `A (= 1) | A (= 2)`
    in an example with two versions for `A`.

2. The version narrowing rule:

        Conflicts: A (<< 2)

    This outright would reject a choice of `A (= 1)`.


So now we have 3 kinds of clauses:

1. package selection
2. version narrowing
3. version selection

If we process them in that order, we should surely be able to find the solution that best matches
the semantics of our Debian dependency model, i.e. selecting earlier choices in a dependency before
later choices in the face of version restrictions.

This still leaves one issue: What if our maintainer did not use `Depends: A (>= 2) | B` but
e.g. `Depends: A (= 3) | B | A (= 2)`. He'd expect us to fall back to B if `A (= 3)` is not
installable, and not to B. But we'd like to enqueue `A` and reject all choices other than `3`
and `2`. I think it's fair to say: "Don't do that, then" here.

## Implementing strict pinning correctly

APT knows a single candidate version per package, this makes the solver relatively deterministic:
It will only ever pick the candidate, or an installed version. This also happens to significantly
reduce the search space which is good - less backtracking. An uptodate system will only ever have
one version per package that can be installed, so we never actually have to choose versions.

But of course, APT allows you to specify a non-candidate version of a package to install, for example:

    apt install foo/oracular-proposed

The way this works is that the core component of the previous solver, which is the `pkgDepCache`
maintains what essentially amounts to an overlay of the policy that you could see with
`apt-cache policy`.

The solver currently however validates allowed version choices against the policy directly,
and hence finds these versions are not allowed and craps out. This is an interesting problem
because the solver should not be dependent on the `pkgDepCache` as the `pkgDepCache` initialization
(`Building dependency tree...`) accounts for about half of the runtime of APT (until the Y/n prompt)
and I'd really like to get rid of it.

But currently the frontend does go via the `pkgDepCache`. It marks the packages in there, building
up what you could call a transaction, and then we translate it to the new solver, and once it is
done, it translates the result back into the `pkgDepCache`.

The current implementation of "allowed version" is implemented by reducing the search space, i.e.
every dependency, we outright ignore any non-allowed versions. So if you have a version 3 of `A`
that is ignored a `Depends: A` would be translated into `A (= 2) | A (= 1)`.

However this has two disadvantages. (1) It means if we show you why `A` could not be installed,
you don't even see `A (= 3)` in the list of choices and (2) you would need to keep the `pkgDepCache`
around for the temporary overrides.

So instead of actually enforcing the allowed version rule by filtering, a more reasonable
model is that we apply the allowed version rule by just marking every other version as not
allowed when discovering the package in the `from depcache` translation layer. This doesn't
really increase the search space either but it solves both our problem of making overrides
work and giving you a reasonable error message that lists all versions of `A`.

## pulling up common dependencies to minimize backtracking cost

One of the common issues we have is that when we have a dependency group

    `A | B | C | D`

we try them in order, and if one fails, we undo everything it did, and move on to the next one. However,
this isn't perhaps the best choice of operation.

I explained before that one thing we do is queue the common dependencies of a package (i.e. dependencies
shared in all versions) when marking a package for install, but we don't do this here: We have already
lowered the representation of the dependency group into a list of versions, so we'd need to extract the
package back out of it.

This can of course be done, but there may be a more interesting solution to the problem, in that we
simply enqueue all the common dependencies. That is, we add `n` backtracking levels for `n` possible
solutions:

1. We enqueue the common dependencies of all possible solutions `deps(A)&deps(B)&deps(C)&deps(D)`
2. We decide (adding a decision level) *not to install D right now* and enqueue `deps(A)&deps(B)&deps(C)`
3. We decide (adding a decision level) *not to install C right now* and enqueue `deps(A)&deps(B)`
4. We decide (adding a decision level) *not to install B right now* and enqueue `A`

Now if we need to backtrack from our choice of `A` we hopefully still have a lot of common dependencies
queued that we do not need to redo. While we have more backtracking levels, each backtracking level
would be significantly cheaper, especially if you have cheap backtracking (which admittedly we do not
have, yet anyway).

The caveat though is: It may be pretty expensive to find the common dependencies. We need to iterate
over all dependency groups of A and see if they are in B, C, and D, so we have a complexity of roughly

`#A * (#B+#C+#D)`

Each dependency group we need to check i.e. is `X|Y` in `B` meanwhile has linear cost: We need to
compare the memory content of two pointer arrays containing the list of possible versions that
solve the dependency group.
This means that `X|Y` and `Y|X` are different dependencies of course, but that is to be expected
-- they are. But any dependency of the same order will have the same memory layout.

So really the cost is roughly `N^4`. This isn't nice.

You can apply various heuristics here on how to improve that, or you can even apply binary logic:

1. Enqueue common dependencies of `A|B|C|D`
2. Move into the left half, enqueue of `A|B`
3. Again divide and conquer and select `A`.

This has a significant advantage in long lists of choices, and also in the common case, where the
first solution should be the right one.

Or again, if you enqueue the package and a version restriction instead, you already get the common
dependencies enqueued for the chosen package at least.

