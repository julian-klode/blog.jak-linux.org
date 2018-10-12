---
author: juliank
date: 2011-04-08 18:15:57+00:00
draft: false
title: 'this week: dh-autoreconf 3, and APT-related things'
type: post
url: /2011/04/08/this-week-dh-autoreconf-3-and-apt-related-things/
categories:
- Debian
---

### Internship / APT stuff



This week was a rather busy week. I'm currently doing a (unpaid) 1 month internship as part of my education. Thanks to Michael Vogt and his boss at Canonical Ltd, this internship takes place in IRC and is dedicated to Debian and Ubuntu stuff, primarily APT-related things.

The first two days were spent on multi-arch support in python-apt: On Monday, I released python-apt 0.7.100.3, introducing initial minimal multi-arch support (just enough to not break anymore, but no really new multi-arch-specific API). This release is also the base for the version going to be shipped in Ubuntu natty, which is one of the reasons to keep the changes such minimal. I also fixed an RC bug related to Python 3.2 modules in python-apt, and implemented nocheck build option and disabled test errors on hurd.

On Tuesday, I released python-apt 0.8.0~exp1 to experimental. This release now has the old-style non-PEP8 API disabled and also introduces improved multi-arch support, by introducing bindings for APT's GrpIterator class, and supporting indexing the cache by (name, architecture) tuples.

On Wednesday, I noticed a strange bug in APT (via python-apt's test suite) where what the cache considered the native architecture was not the configured one. David Kalnischkies and I debugged the problem, and he found the source of the problem and implemented a fix in his branch of APT. I also introduced multi-arch support for the aptsources module, fixed all Python 3.2 ResourceWarnings in python-apt, and prepared an NMU for python-debian, to adjust it to python-apt's new API. I also took over maintenance  of  software-properties in Debian, and did two uploads there (rebased on the Ubuntu package), both with python-apt 0.8 API support.

On Thursday, I shifted a bit more to the Ubuntu side and fixed several bugs in APT and aptdaemon, resulting in the aptdaemon 0.41+bzr614-0ubuntu2 upload and apt 0.8.13.3ubuntu2. I also fixed software-properties KDE version in Debian, as I broke it the previous day.

Today, on Friday, I fixed one more bug in APT. APT now treats Release files that cannot be verified identical to Release files without signature, that is, they are actually parsed now (no more missing Origin fields) - see [LP: #704595](https://bugs.launchpad.net/ubuntu/+source/apt/+bug/704595).



### dh-autoreconf 3


I uploaded dh-autoreconf 3, fixing all bugs in the BTS except for one (if someone knows why autopoint depends on git, please tell me, and I may fix this bug as well). For those who don't know dh-autoreconf, it is a tool to run autoreconf automatically during the package build, so no need for manual cleanup or autoreconf patches.

I now thought about adding the option to automatically patch ltmain.sh to dh-autoreconf. As many know, ltmain.sh does not work correctly with -Wl,--as-needed. Now, if the libtool maintainer cooperates and provides a patch file in the libtool binary package, dh-autoreconf could automatically apply it during build-time, thus fixing this problem as well.



### GNOME 3


I'm now running GNOME 3, or the parts of it we have in Debian.




### Next week


We'll probably see python-apt 0.8.0~exp2 next week with more improved multi-arch support and other fixes.


