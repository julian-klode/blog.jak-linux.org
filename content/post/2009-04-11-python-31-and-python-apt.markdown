---
author: juliank
date: 2009-04-11 20:28:04+00:00
draft: false
title: Python 3.1 and python-apt
type: post
url: /2009/04/11/python-31-and-python-apt/
categories:
- Debian
- Python
---

So, I have started to port python-apt to Python 3. Most things work already, but there is one single problem. I can not access the attributes of the objects, only their methods.

In Python 2.5, everything works perfectly. In Python 3.1, the same code produces an error. An example is `apt_pkg.GetCache().Packages`. I defined the slots `tp_getattro` and `tp_methods`. In Python 3.1, tp_getattro seems to be ignored.

If you want to help,
[http://bzr.debian.org/loggerhead/users/jak/python-apt/py3k/changes](http://bzr.debian.org/loggerhead/users/jak/python-apt/py3k/changes) for browsing the branch and [http://bzr.debian.org/users/jak/python-apt/py3k/](http://bzr.debian.org/users/jak/python-apt/py3k/) for branching it.

This branch contains the current state and allows you to build a python-apt package shipping with Python 3.1 modules and extensions. But as I wrote above, not everything works yet. But its far enough for about 5 hours of work.

**Update 2009-04-12 00:17 CEST**: I just fixed a bunch of problems, including the one listed above. Most of python-apt should work now, including the 'apt' package.
