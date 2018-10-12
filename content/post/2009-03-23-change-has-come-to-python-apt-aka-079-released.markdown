---
author: juliank
date: 2009-03-23 15:26:31+00:00
draft: false
title: Change has come to python-apt - aka 0.7.9 released
type: post
url: /2009/03/23/change-has-come-to-python-apt-aka-079-released/
categories:
- Debian
---

With version 0.7.9 "change has come" to python-apt, and I will tell you now what the new stuff is about:


## 1. Introduction of the documentation


As you may know, python-apt 0.7.8's only documentation was available from the source code and to some parts from the docstrings. This changed in python-apt 0.7.9~exp2, when I introduced a complete documentation written in reStructuredText, and generated using Sphinx. This documentation has even improved in the final 0.7.9 release, and I will push it to the online mirror at [http://apt.alioth.debian.org/python-apt-doc/](http://apt.alioth.debian.org/python-apt-doc/) soon (it currently still has 0.7.9~exp2).


## 2. Graphical Progress


The module apt.progress.gtk2 provides widgets for Python GTK+ coders, allowing them to easily build graphical applications interacting directly with apt. I am still looking for someone to write a apt.progress.qt4 module, if no one wants to do this, I will do it myself.


## 3. Enhanced apt.debfile module


A lot of code has been merged from gdebi, now allowing to do a large set of operations on local .deb files. For example, you can now install these packages. This module is also the first module to follow PEP8 naming conventions (lowercase_with_underscores), the others will be adapted at a later point.


## 4. Complete code cleanup


I have worked on cleaning up the whole code, fixing white space problems, and more. Ben Finney was very helpful, I merged some of his patches for whitespace. I also fixed several other problems related to PEP8 conformance. Previously the PEP8 checking tool (see documentation) found about possible 964 issues, this has been reduced to 7 (-957), but these 7 'issues' are simply the usage of has_key() at locations where it can't be avoided [interfacing with TagSection objects], i.e. they are false positives.


## 5. Introduction of apt.package.Version


In python-apt 0.7.9 I am introducing a new class apt.package.Version. This class provides access to various attributes of a version, like the record, the version number, the origin and even allows you to fetch the corresponding source code. But one of the best things about it is that it is sortable, allowing you to write:

    
    print 'Highest bash version:', max(apt.Cache()['bash'].versions)


This makes it very clear that you can build really cool applications with it. The various candidate*() and installed*() methods of apt.Package objects haven been deprecated, and you should use the Version() objects available via Package.installed or Package.candidate properties.


## Summary


All in all, the python-apt 0.7.9 is a big step forward. It is one of the largest releases in the history of python-apt and provides various new features to make developing easier. With all the code cleanups, and the documentation, you should be able to find everything you need; if not please report a bug. When we are asked "Can we do this with python-apt?", we can finally say: "Yes we can!"
