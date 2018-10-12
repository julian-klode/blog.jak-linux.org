---
author: juliank
date: 2010-01-20 16:52:13+00:00
draft: false
title: python-apt 0.7.93 just hit unstable.
type: post
url: /2010/01/20/python-apt-0-7-93-just-hit-unstable/
categories:
- Debian
---

I just uploaded python-apt 0.7.93 to unstable with support for Python 2.6 and Python 3.1, meaning that there is now a single development branch again.

This uploads brings developers the new API with real classes in apt_pkg (you can now use pydoc to view documentation), C++ bindings for making apt-pkg applications scriptable (although they should be considered experimental), a test suite (although aptsources fails in one test for now) and many new context managers for enhanced Python 3 coding fun. And objects are now freed when their reference count reaches 0. A more complete list of news can be found in the [What’s New In python-apt 0.7.100](http://apt.alioth.debian.org/python-apt-doc/whatsnew/0.7.100.html) part of the documentation.

For the next releases until 0.7.100 release, the focus is clearly on fixing bugs and improving the documentation. We need more tests of the Python 3 builds, especially in areas dealing with str and unicode stuff.

Have fun, read the [documentation](http://apt.alioth.debian.org/python-apt-doc/), and code.
