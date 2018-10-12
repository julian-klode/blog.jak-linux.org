---
author: juliank
date: 2008-04-17 15:37:59+00:00
draft: false
title: python-libisofs 0.0.1 available
type: post
url: /2008/04/17/python-libisofs-001-available/
categories:
- Debian
- General
- Python
- Ubuntu
---

A first preview of the python-libisofs bindings is available now. It's currently located in a git branch at git.debian.org, but this may change at a later point.

The bindings support the creation of ISO Images and  (almost) all options libisofs supports, like Rockridge, Joliet, and much more. Reading and Modifying existing images is not supported yet.

The code is written in Cython and you need cython installed for building from the git branch. It can be installed just like any other Python module/extension/package, using a setup.py.

Browse: [http://git.debian.org/?p=users/jak-guest/python-libisofs.git](http://git.debian.org/?p=users/jak-guest/python-libisofs.git)
Get: git clone git://git.debian.org/git/users/jak-guest/python-libisofs.git

I'll package it for Debian within the next weeks after some further tests.
