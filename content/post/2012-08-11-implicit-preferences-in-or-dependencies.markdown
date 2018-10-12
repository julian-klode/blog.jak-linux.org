---
author: juliank
date: 2012-08-11 14:27:18+00:00
draft: false
title: Implicit preferences in OR dependencies
type: post
url: /2012/08/11/implicit-preferences-in-or-dependencies/
categories:
- APT2
- Debian
- General
---

Debian packages commonly use or dependencies of the form "a | b" to mean that a or b should be installed, while preferring option a over b. In general, for resolving an or dependency, we will try all options from the left to the right, preferring the left-most option. We also prefer real packages over virtual ones. If one of the alternatives is already installed we use that.


    
    
    def solve_or(or):
      best_real = None
      best_virtual = None
      for dep in or:
         for target in dep:
            if target.name == dep.name and best_real is None:
               best_real = target
            if target.name != dep.name and best_virtual is None:
               best_virtual = target        
            if target.is_installed():
              return target
    
      return best_real if best_real is not None else best_virtual
    



Now, this way of solving dependencies is slightly problematic. Let us consider a package that depends on: a | b, b. APT will likely choose to install 'a' to satisfy the first dependency and 'b' to satisfy the second. I currently have draft  code around for a future version of APT that will cause it to later on revert unneeded changes, which means that APT will then only install 'b'. This result closely matches the CUDF solvers and cupt's solver.

On the topic of solving algorithms, we also have the problem that optimizing solvers like the ones used with apt-cudf do not respect the order of dependencies, rather choosing to minimise the number of packages installed. This causes such a solver to often do stuff like selecting an sqlite database as backend for some service rather then a larger SQL server, as that installs fewer packages.

To make such solvers aware of the implicit preferences, we can introduce a new type of dependency category: Weak conflicts, also known as Recommends-Not. If a package P defines a Recommends-Not dependency against a package Q, then this means that Q should not be installed if P is installed. Now, if we have a dependency like:

`Depends: a | b | c`

we can encode this as:

`Recommends-Not: c, c, b`

Causing the solver to prefer a, then b, and then c. This should be representable as a pseudo-boolean optimization problem, as is common for the dependency problem, although I have not looked at that yet -- it should work by taking the standard representation of conflicts, adding a relaxation variable and then minimising [or maximising] the number of relaxation variables.
