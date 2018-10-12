---
author: juliank
date: 2009-08-18 15:27:06+00:00
draft: false
title: Python APT 0.7.92 released
type: post
url: /2009/08/18/python-apt-0-7-92-released/
categories:
- Debian
---

The release of Python APT 0.7.92 is the first (pre-)release to introduce the new C++ bindings to create Python objects for almost every C++ object in the apt-pkg and apt-inst libraries. It is also the first version of python-apt which correctly deallocates its objects. It also introduces classes in apt_inst which are modelled after the 'tarfile' module in Python. The new progress classes behave more like the ones in apt, which allows you to write even more perfect apt-get clones (if you want to). There are also several new classes and functions.

I expect this pre-release to be one of the most buggiest in the 0.8 series, because it changes a lot of the core stuff, like memory management. The release is currently waiting in NEW due to the new python-apt-dev package, if you want to test it, you can use the repository at [http://people.debian.org/~jak/debian/experimental/](http://people.debian.org/~jak/debian/experimental/), where the source package and the binaries for amd64 are provided. Most applications should continue to work with python-apt 0.7.92, if you find a non-working application, report a bug (unless its an error related to apt_pkg.Version, which has been renamed to apt_pkg.VERSION due to naming conflicts).

The next release should hopefully reach RC-quality. It will primarily focus on documentation updates (there is a lot of stuff missing and parts are wrong currently) and bugfixing, but will also introduce the new Qt4 progress classes. The next release will also feature the ABI and API freezes. It is scheduled for release in September (next month), and 0.8 is scheduled for October.

For further information, you can send me an email or ask in #debian-apt on OFTC.
