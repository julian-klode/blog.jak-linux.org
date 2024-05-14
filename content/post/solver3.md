---
title: "The new APT 3.0 solver"
date: 2024-05-14T13:26:05+02:00
---
APT 2.9.3 introduces the first iteration of the new solver codenamed
solver3, and now available with the --solver 3.0 option. The new solver
works fundamentally different from the old one.


## How does it work?

Solver3 is a fully backtracking dependency solving algorithm that defers
choices to as late as possible. It starts with an empty set of packages,
then adds the manually installed packages, and then installs packages
automatically as necessary to satisfy the dependencies.

Deferring the choices is implemented multiple ways:

First, all install requests
recursively mark dependencies with a single solution for install, and any
packages that are being rejected due to conflicts or user requests will
cause their reverse dependencies to be transitively marked as rejected,
provided their or group cannot be solved by a different package.

Second, any dependency with more than one choice is pushed to a priority
queue that is ordered by the number of possible solutions, such that we
resolve a|b before a|b|c.

Not *just* by the number of solutions, though. One important point to
note is that optional dependencies, that is, Recommends, are always
sorting after mandatory dependencies. Do note on that: Recommended
packages do not "nest" in backtracking - dependencies of a Recommended
package themselves are not optional, so they will have to be resolved
before the next Recommended package is seen in the queue.

Another important step in deferring choices is extracting the common
dependencies of a package across its version and then installing them
before we even decide which of its versions we want to install - one
of the dependencies might cycle back to a specific version after all.

Decisions about package levels are recorded at a certain decision level,
if we reach a conflict we backtrack to the previous decision level,
mark the decision we made (install X) in the inverse (DO NOT INSTALL X),
reset all the state all decisions made at the higher level, and restore
any dependencies that are no longer resolved to the work queue.

## Comparison to SAT solver design.

If you have studied SAT solver design, you'll find that essentially
this is a DPLL solver without pure literal elimination. A pure literal
eliminitation phase would not work for a package manager: First negative
pure literals (packages that everything conflicts with) do not exist,
and positive pure literals (packages nothing conflicts with) we do not want
to mark for install - we want to install as little as possible (well subject,
to policy).

As part of the solving phase, we also construct an implication graph, albeit
a partial one: The first package installing another package is marked as the
reason (A -> B), the same thing for conflicts (not A -> not B).

Once we have added the ability to have multiple parents in the implication
graph, it stands to reason that we can also implement the much more advanced
method of conflict-driven clause learning; where we do not jump back to the
previous decision level but exactly to the decision level that caused the
conflict. This would massively speed up backtracking.

## What changes can you expect in behavior?

The most striking difference to the classic APT solver is that solver3 always keeps
manually installed packages around, it never offers to remove them. We will relax that
in a future iteration so that it can *replace* packages with new ones, that is, if your
package is no longer available in the repository (obsolete), but there is one that
Conflicts+Replaces+Provides it, solver3 will be allowed to install that and remove the
other.

Implementing that policy is rather trivial: We just need to queue `obsolete | replacement`
as a dependency to solve, rather than mark the obsolete package for install.

Another critical difference is the change in the autoremove behavior: The new solver
currently only knows the strongest dependency chain to each package, and hence it will
not keep around any packages that are only reachable via weaker chains.
A common example is when `gcc-<version>` packages accumulate on your system over the
years. They all have `Provides: c-compiler` and the `libtool` `Depends: gcc | c-compiler`
is enough to keep them around.

# New features

The new option `--no-strict-pinning` instructs the solver to consider all versions of
a package and not just the candidate version. For example, you could use `apt install foo=2.0 --no-strict-pinning`
to install version 2.0 of foo and upgrade - or downgrade - packages as needed to satisfy `foo=2.0` dependencies.
This mostly comes in handy in use cases involving Debian experimental or the Ubuntu proposed pockets, where you
want to install a package from there, but try to satisfy from the normal release as much as possible.

The implication graph building allows us to implement an `apt why` command, that while not as nicely
detailed as aptitude, at least tells you the exact reason why a package is installed. It will only show
the strongest dependency chain at first of course, since that is what we record.

## What is left to do?

At the moment, error information is not stored across backtracking in any way, but we generally
will want to show you the first conflict we reach as it is the most natural one; or all conflicts.
Currently you get the last conflict which may not be particularly useful.

Likewise, errors currently are just rendered as implication graphs of the form `[not] A -> [not] B -> ...`,
and we need to put in some work to present those nicely.

The test suite is not passing yet, I haven't really started working on it. A challenge is that most
packages in the test suite are manually installed as they are mocked, and the solver now doesn't remove
those.

We plan to implement the replacement logic such that foo can be replaced by `foo2 Conflicts/Replaces/Provides foo`
without needing to be automatically installed.

Improving the backtracking to be non-chronological conflict-driven clause learning would vastly
enhance our backtracking performance. Not that it seems to be an issue right now in my limited
testing (mostly noble 64-bit-time_t upgrades). A lot of that complexity you have normally is not
there because the manually installed packages and resulting unit propagation (single-solution
Depends/Reverse-Depends for Conflicts) already ground us fairly far in what changes we can actually make.

Once all the stuff has landed, we need to start rolling it out and gather feedback. On Ubuntu I'd like
automated feedback on regressions (running solver3 in parallel, checking if result is worse and then
submitting an error to the error tracker), on Debian this could just be a role email address to send
solver dumps to.

At the same time, we can also incrementally start rolling this out. Like phased updates in Ubuntu,
we can also roll out the new solver as the default to 10%, 20%, 50% of users before going to the
full 100%. This will allow us to capture regressions early and fix them.

