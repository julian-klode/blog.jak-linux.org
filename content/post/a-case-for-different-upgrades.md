---
title: "Divergence - A case for different upgrade approaches"
date: 2023-10-10T19:22:49+02:00
---

APT currently knows about three types of upgrades:

- upgrade without new packages (apt-get upgrade)
- upgrade with new packages (apt upgrade)
- upgrade with new packages and deletions (apt{,-get} {dist,full}-upgrade)

All of these upgrade types are necessary to deal with upgrades within a
distribution release. Yes, sometimes even removals may be needed because
bug fixes require adding a Conflicts somewhere.

In Ubuntu we have a third type of upgrades, handled by a separate tool: release
upgrades. `ubuntu-release-upgrader` changes your sources.list, and applies various
quirks to the upgrade.

In this post, I want to look not at the quirk aspects but discuss how dependency
solving should differ between intra-release and inter-release upgrades.

Previous solver projects (such as Mancoosi) operated under the assumption that minimizing
the number of changes performed should ultimately be the main goal of a solver. This makes
sense as every change causes risks.
However it ignores a different risk, which especially applies when upgrading from one
distribution release to a newer one: Increasing divergence from the norm.

Consider a person installs `foo` in Debian 12. `foo` depends on `a | b`, so `a` will
be automatically installed to satisfy the dependency. A release later, `a` has some
known issues and `b` is prefered, the dependency now reads: `b|a`.

A classic solver would continue to keep `a` installed because it was installed before,
leading upgraded installs to have `foo, a` installed whereas new systems have `foo, b`
installed. As systems get upgraded over and over, they continue to diverge further and
further from new installs to the point that it adds substantial support effort.

My proposal for the new APT solver is that when we perform release upgrades, we forget
which packages where previously automatically installed. 
We effectively perform a normalization: All systems with the same set of manually installed packages will end up with the same set of automatically installed packages.
Consider the solving starting with an empty set and then installing the latest version of each previously manually installed package: It will see now that `foo` depends
`b|a` and install `b` (and `a` will be removed later on as its not part of the solution).

Another case of divergence is `Suggests` handling. Consider that `foo` also Suggests
`s`. You now install another package `bar` that depends `s`, hence `s` gets installed.
Upon removing `bar`, `s` is not being removed automatically because `foo` still suggests
it (and you may have grown used to `foo`'s integration of `s`). This is because apt considers
Suggests to be important - they won't be automatically installed, but will not be automatically
removed.

In Ubuntu, we unset that policy on release upgrades to normalize the systems. The reasoning
for that is simple: While you may have grown to use `s` as part of `foo` during the release,
an upgrade to the next release already is big enough that removing `s` is going to have
less of an impact - breakage of workflows is expected between release upgrades.

I believe that `apt release-upgrade` will benefit from both of these design choices,
and in the end it boils down to a simple mantra:

- On upgrades within a release, minimize changes.
- On upgrades between releases, minimize divergence from fresh installs.

