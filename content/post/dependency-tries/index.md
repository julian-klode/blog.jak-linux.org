---
title: "Dependency Tries"
date: 2025-09-27T16:32:19+02:00
---

As I was shopping groceries I had a shocking realization: The active dependencies
of packages in a solver actually form a trie (a dependency `A|B` of a package `X`
is considered active if we marked `X` for install).

Consider the dependencies `A|B|C`, `A|B`, `B|X`. In Debian packages, or expresses a
preference relationship between its operands, so in `A|B|C`, `A` is preferred over `B`
and `B` over `C` (and `A` transitively over `C`).

This means that we can convert the three dependencies into a trie as follows:

![Dependency trie of the three dependencies](trie1.svg)

Solving the dependency here becomes a matter of trying to install the package
referenced by the first edge of the root, and seeing if that sticks. In this
case, that would be 'a'. Let's assume that 'a' failed to install, the next
step is to remove the empty node of `a`, and merging its children into the
root.


![Reduced dependency trie with "not A" containing b, b|c, b|x](trie2.svg)

For ease of visualisation, we remove "a" from the dependency nodes as well,
leading us to a trie of the dependencies "b", "b|c", and "b|x".

Presenting the Debian dependency problem, or the positive part of it as a
trie allows us for a great visualization of the problem but it may not proof
to be an effective implementation choice.

