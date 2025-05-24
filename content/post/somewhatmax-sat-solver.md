---
title: "A SomewhatMaxSAT Solver"
date: 2025-05-24T12:15:50+02:00
---

**As you may recall** from previous posts and elsewhere I have been busy writing a new solver for APT.
Today I want to share some of the latest changes in how to approach solving.

The idea for the solver was that manually installed packages are always protected from removals --
in terms of SAT solving, they are facts. Automatically installed packages become optional unit
clauses. Optional clauses are solved after manual ones, they don't partake in normal unit propagation.

This worked fine, say you had

```
A                                   # install request for A
B                                   # manually installed, keep it
A depends on: conflicts-B | C
```

Installing `A` on a system with `B` installed installed `C`, as it was not allowed to
install the `conflicts-B` package since `B` is installed.

**However,** I also introduced a mode to allow removing manually installed packages, and that's
where it broke down, now instead of `B` being a fact, our clauses looked like:

```
A                               # install request for A
A depends on: conflicts-B | C
Optional: B                     # try to keep B installed
```

As a result, we installed `conflicts-B` and removed `B`; the steps the solver takes are:

1. `A` is a fact, mark it
1. `A depends on: conflicts-B | C` is the strongest clause, try to install `conflicts-B`
1. We unit propagate that `conflicts-B` conflicts with `B`, so we mark `not B`
1. `Optional: B` is reached, but not satisfiable, ignore it because it's optional.

This isn't correct: Just because we allow removing manually installed packages doesn't mean that we should remove manually installed packages if we don't need to.


**Fixing** this turns out to be surprisingly easy. In addition to adding our optional (soft) clauses, let's first assume all of them!

But to explain how this works, we first need to explain some terminology:

1. The solver operates on a stack of decisions
1. "enqueue" means a fact is being added at the current decision level, and enqueued for propagation
1. "assume" bumps the decision level, and then enqueues the assumed variable
1. "propagate" looks at all the facts and sees if any clause becomes unit, and then enqueues it
1. "unit" is when a clause has a single literal left to assign


To illustrate this in pseudo Python code:

1. We introduce all our facts, and if they conflict, we are unsat:

    ```python3
    for fact in facts:
        enqueue(fact)
    if not propagate():
        return False
    ```

2. For each optional literal, we register a soft clause and assume it. If the assumption fails,
   we ignore it. If it succeeds, but propagation fails, we undo the assumption.

    ```python3
    for optionalLiteral in optionalLiterals:
        registerClause(SoftClause([optionalLiteral]))
        if assume(optionalLiteral) and not propagate():
            undo()
    ```

3. Finally we enter the main solver loop:

    ```python3
    while True:
        if not propagate():
            if not backtrack():
                return False
        elif <all clauses are satisfied>:
            return True
        elif it := find("best unassigned literal satisfying a hard clause"):
            assume(it)
        elif it := find("best unassigned literal satisfying a soft clause"):
            assume(it)
    ```

The key point to note is that the main loop will undo the assumptions in order; so
if you assume `A,B,C` and `B` is not possible, we will have also undone `C`. But since
`C` is also enqueued as a soft clause, we will then later find it again:

1. Assume `A`: `State=[Assume(A)]`, `Clauses=[SoftClause([A])]`
1. Assume `B`: `State=[Assume(A),Assume(B)]`, `Clauses=[SoftClause([A]),SoftClause([B])]`
1. Assume `C`: `State=[Assume(A),Assume(B),Assume(C)]`, `Clauses=[SoftClause([A]),SoftClause([B]),SoftClause([C])]`
1. Solve finds a conflict, backtracks, and sets `not C`: `State=[Assume(A),Assume(B),not(C)]`
1. Solve finds a conflict, backtracks, and sets `not B`: `State=[Assume(A),not(B)]` -- C is no longer assumed either
1. Solve, assume `C` as it satisfies `SoftClause([C])` as next best literal: `State=[Assume(A),not(B),Assume(C)]`
1. All clauses are satisfied, solution is `A`, `not B`, and `C`.

**This is not (correct) MaxSAT**, because we actually do not guarantee that we satisfy as many soft clauses as possible. Consider you have the following clauses:

    Optional: A
    Optional: B
    Optional: C
    B Conflicts with A
    C Conflicts with A

There are two possible results here:

1. `{A}`   -- If we assume `A` first, we are unable to satisfy `B` or `C`.
2. `{B,C}` -- If we assume either `B` or `C` first, `A` is unsat.

The question to ponder though is whether we actually need a global maximum or whether a local maximum is satisfactory in practice for a dependency solver
If you look at it, a naive MaxSAT solver needs to run the SAT solver `2**n` times for `n` soft clauses, whereas our heuristic only needs `n` runs.

For dependency solving, it seems we do not seem have a strong need for a global maximum:
There are various other preferences between our literals, say priorities;
and empirically, from evaluating hundreds of regressions *without* the initial assumptions,
I can say that the assumptions do fix those cases and the result is correct.

**Further improvements** exist, though, and we can look into them if they are needed, such as:

- Use a *better heuristic*:

   If we assume 1 clause and solve, and we cause 2 or more clauses to become unsatisfiable,
   then that clause is a local minimum and can be skipped.
   This is a more common heuristical MaxSAT solver.
   This gives us a *better* local maximum, but not a global one.

   This is more or less what the [Smart package manager](https://labix.org/smart) did,
   except that in Smart, all packages were optional, and the entire solution was scored. 
   It calculated a basic solution without optimization and then toggled each variable and saw if the score improved.

-  Implement *an actual search for a global maximum*:

   This involves reading the literature.
   There are various versions of this, for example:
   1. Find unsatisfiable cores and use those to guide relaxation of clauses.
   2. A bounds-based search, where we translate sum(satisifed clauses) > k into SAT, and then search in one of the following ways:

         1. from 0 upward
         2. from n downward
         2. perform a binary search on [0, k] satisfied clauses.

      *Actually* we do not even need to calculate sum constraints into CNF, because we can just add a specialized new type of constraint to our code.
