---
author: juliank
date: 2009-01-10 17:38:10+00:00
draft: false
title: python-apt documentation - 2nd time
type: post
url: /2009/01/10/python-apt-documentation-2nd-time/
categories:
- Debian
- Python
---

News: [http://bzr.debian.org/loggerhead/users/jak/python-apt/jak/revision/219](http://bzr.debian.org/loggerhead/users/jak/python-apt/jak/revision/219)
 
introduced again some new documentation.

doc/source/apt/debfile.rst            |    6
doc/source/apt_pkg/cache.rst          |  540 +++++++++++++++++++++++++++++++++-
doc/source/apt_pkg/index.rst          |   24 +
doc/source/conf.py                    |    5
doc/source/examples/cache-packages.py |   22 +
doc/source/examples/cache-pkgfile.py  |   29 +
doc/source/examples/missing-deps.py   |   51 +++

7 files changed, 659 insertions(+), 18 deletions(-)

You can see them at [http://people.debian.org/~jak/python-apt-doc/](http://people.debian.org/~jak/python-apt-doc/)

Missing seem to be:
 - AcquireFile
 - AcquireItem
 - ActionGroup
 - Configuration
 - MetaIndex
 - PackageIndexFile
 - PkgManager
 - PkgRecords
 - PkgSourceList
 - PkgSrcRecords
 - ProblemResolver
 - TagFile
 - TagSection

But the weekend is not over yet. I will blog tomorrow again, and once I'm finished with everything (which may be tomorrow, too). 

Have fun, read the documentation, find the mistakes. Some things are currently written as '???', if you know what fits there, please tell me.
