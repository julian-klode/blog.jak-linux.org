---
title: "Sound Removals"
date: 2025-10-18T21:37:17+02:00
---

## Problem statement
Currently if you have an automatically installed package A (= 1) where

- A (= 1) Depends B (= 1)
- A (= 2) Depends B (= 2)

and you upgrade B from 1 to 2; then  you can:

1. Remove A (= 1)
2. Upgrade A to version 2

If A was installed by a chain initiated by Recommends (say X Rec Y, Y Depends A), the solver sometimes preferred removing A (and anything depending on it until it got).

I have a fix pending to introduce eager Recommends which fixes the practical case, but
this is still not _sound_.

In fact we can show that the solver produces the wrong result for small
minimal test cases, as well as the right result for some others without the
fix (hooray?).

Ensuring sound removals is more complex, and first of all it begs the question: When
is a removal sound? This, of course, is on us to define.

An easy case can be found in the [Debian policy, 7.6.2 "Replacing whole packages, forcing their removal"](https://www.debian.org/doc/debian-policy/ch-relationships.html#replacing-whole-packages-forcing-their-removal):

If `B (= 2)` declares a `Conflicts: A (= 1)` and `Replaces: A (= 1)`, then the removal
is valid. However this is incomplete as well, consider it declares `Conflicts: A (< 1)`
and `Replaces: A (< 1)`; the solution to remove A rather than upgrade it would still
be wrong.

This indicates that we should only allow removing `A` if the conflicts could not be solved
by upgrading it.

The other case to explore is package removals. If B is removed, A should be removed as well;
however it there is another package X that `Provides: B (= 1)` and it is marked for install,
A should not be removed. That said, the solver is not allowed to install X to satisfy the
depends `B (= 1)` - only to satisfy other dependencies [we do not want to get into endless
loops where we switch between alternatives to keep reverse dependencies installed].

## Proposed solution
To solve this, I propose the following definition:

**Definition (sound removal)**: A removal of package `P` is sound if either:

1. A version `v` is installed that *package-conflicts* with B.
2. A package `Q` is removed and the installable versions of P *package-depends* on Q.

where the other definitions are:

**Definition (installable version)**: A version `v` is installable if either it is installed,
or it is newer than an installed version of the same package (you may wish to change this to
accomodate downgrades, or require strict pinning, but here be dragons).

**Definition (package-depends):** A version `v` *package-depends* on a package B if either:

1. there exists a dependency in `v` that can be solved by any version of `B`, or
2. there exists a package `C` where `v package-depends C` and `any (c in C) package-depends B` (transitivity)


**Definition (package-conflicts):** A version `v` *package-conflicts* with an installed package `B` if either:

1. it declares a conflicts against an installable version of B; or
2. there exists a package `C` where `v package-conflicts C`, 
   and `b package-depends C` for installable versions b.

## Translating this into a (modified) SAT solver

One approach may be to implement the logic in the conflict analysis that drives backtracking, i.e.
we assume a package `A` and when we reach `not A`, we analyse if the implication graph for `not A`
constitutes a sound removal, and then replace the assumption `A` with the assumption
`A or "learned reason`.

However, while this seems a plausible mechanism for a DPLL solver, for a modern CDCL solver,  it's
not immediately evident how to analyse whether `not A` is sound if the reason for it is a learned
clause, rather than a problem clause.

Instead we propose a static encoding of the rules into a slightly modified SAT solver:

Given c1, ..., cn that transitive-conflicts A and D1, ..., Dn that A package-depends on,
introduce the rule:


`A unless c1 or c2 or  ... cn ... or not D1 or not D2 ... or not Dn`

Rules of the form `A... unless B...` - where `A...` and `B...` are CNF - are
intuitively the same as `A... or B...`, however the semantic here is different:
We are not allowed to select `B...` to satisfy this clause.

This requires a SAT solver that tracks a reason for each literal being assigned,
such as solver3, rather than a SAT solver like MiniSAT that only tracks reasons across
propagation (solver3 may track `A depends B or C` as the reason for `B` without evaluating
`C`, whereas MiniSAT would only track it as the reason given `not C`).

## Is it actually sound?

The proposed definition of a sound removal may still proof unsound as I either missed
something in the conclusion of the proposed definition that violates my goal I set out
to achieve, or I missed some of the goals.

I challenge you to find cases that cause removals that look wrong :D
