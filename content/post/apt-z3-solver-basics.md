---
title: "APT Z3 Solver Basics"
date: 2021-11-21T20:49:34+01:00
---

[Z3](https://github.com/Z3Prover/z3) is a theorem prover developed at Microsoft research and available as
a dynamically linked C++ library in Debian-based distributions. While the
library is a whopping 16 MB, and the solver is a tad slow, it's permissive
licensing, and number of tactics offered give it a huge potential for use
in solving dependencies in a wide variety of applications.

Z3 does not need normalized formulas, but offers higher level abstractions
like `atmost` and `atleast` and `implies`, that we will make use of together
with boolean variables to translate the dependency problem to a form Z3
understands.

In this post, we'll see how we can apply Z3 to the dependency resolution
in APT. We'll only discuss the basics here, a future post will explore
optimization criteria and recommends.

## Translating the universe

APT's package universe consists of 3 relevant things: packages (the tuple
of name and architecture), versions (basically a .deb), and dependencies
between versions.

While we could translate our entire universe to Z3 problems, we instead will
construct a root set from packages that were manually installed and versions
marked for installation, and then build the transitive root set from it by
translating all versions reachable from the root set.

For each package P in the transitive root set, we create a boolean literal `P`. We then
translate each version P1, P2, and so on. Translating a version means building
a boolean literal for it, e.g. `P1`, and then translating the dependencies as shown below.

We now need to create two more clauses to satisfy the basic requirements for debs:

1. If a version is installed, the package is installed; and vice versa. We can encode
   this requirement for P above as `P == atleast({P1,P2}, 1)`.
2. There can only be one version installed. We add an additional constraint of the
   form `atmost({P1,P2}, 1)`.

We also encode the requirements of the operation.

1. For each package P that is manually installed, add a constraint `P`.
1. For each version V that is marked for install, add a constraint `V`.
1. For each package P that is marked for removal, add a constraint `!P`.

### Dependencies

Packages in APT have dependencies of two basic forms: Depends and Conflicts,
as well as variations like Breaks (identical to Conflicts in solving terms),
and Recommends (soft Depends) - we'll ignore those for now. We'll discuss
Conflicts in the next section.

Let's take a basic dependency list: `A Depends: X|Y, Z`. To represent that
dependency, we expand each name to a list of versions that can satisfy
the dependency, for example `X1|X2|Y1, Z1`.

Translating this dependency list to our Z3 solver, we create boolean variables
`X1,X2,Y1,Z1` and define two rules:

1. `A implies atleast({X1,X2,Y1}, 1)`
2. `A implies atleast({Z1}, 1)`

If there actually was nothing that satisfied the Z requirement, we'd have added
a rule `not A`. It would be possible to simply not tell Z3 about the version at
all as an optimization, but that adds more complexity, and the `not A` constraint
should not cause too many problems.

### Conflicts

Conflicts cannot have `or` in them. A dependency `B Conflicts: X, Y` means that only
one of B, X, and Y can be installed. We can directly encode this in Z3 by using the
constraint `atmost({B,X,Y}, 1)`. This is an optimized encoding of the constraint: We
could have encoded each conflict in the form `!B or !X`, `!B or !X`, and so on. Usually
this leads to worse performance as it introduces additional clauses.

## Complete example

Let's assume we start with an empty install and want to install the package `a` below.

```
Package: a
Version: 1
Depends: c | b

Package: b
Version: 1

Package: b
Version: 2
Conflicts: x

Package: d
Version: 1

Package: x
Version: 1
```

The translation in Z3 rules looks like this:

1. Package rules for `a`:
    1. `a == atleast({a1}, 1)` - package is installed iff one version is
    1. `atmost({a1}, 1)` - only one version may be installed
    1. `a` -- a must be installed
1. Dependency rules for `a`
    1. `implies(a1, atleast({b2, b1}, 1))` -- the translated dependency above. note that `c` is gone, it's not reachable.
1. Package rules for `b`:
    1. `b == atleast({b1,b2}, 1)` - package is installed iff one version is
    1. `atmost({b1, b2}, 1)` - only one version may be installed
1. Dependencies for `b (= 2)`:
    1. `atmost({b2, x1}, 1)` - the conflicts between x and b = 2 above
1. Package rules for `x`:
    1. `x == atleast({x1}, 1)` - package is installed iff one version is
    1. `atmost({x1}, 1)` - only one version may be installed

The package `d` is not translated, as it is not reachable from the root
set `{a1}`, the transitive root set is `{a1,b1,b2,x1}`.

## Next iteration: Optimization

We have now constructed the basic set of rules that allows us to
solve solve our dependency problems (equivalent to SAT), however
it might lead to suboptimal solutions where it removes automatically
installed packages, or installs more packages than necessary, to
name a few examples.

In our next iteration, we have to look at introducing optimization;
for example, have the minimum number of removals, the minimal
number of changed packages, or satisfy as many recommends as possible.
We will also look at the upgrade problem (upgrade as many packages as
possible), the autoremove problem (remove as many automatically installed
packages as possible).
