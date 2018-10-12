---
author: juliank
date: 2010-08-11 20:22:36+00:00
draft: false
title: APT2 - this time in C
type: post
url: /2010/08/11/apt2-this-time-in-c/
categories:
- APT2
---

As I wrote a few hours ago on deity@l.d.o (see [http://lists.debian.org/deity/2010/08/msg00057.html](http://lists.debian.org/deity/2010/08/msg00057.html)), APT2 is back again. The first time, I tried Vala; but this time I wrote it in C (with the help of GLib, but no GObject) and the cache uses GVariant instead of an SQLite database. It's really basic at the moment (no solver, package installation/removal), but it will improve. Read operation should be faster than with APT, although writes are slower (this will be fixed by reusing unchanged parts of the cache).

See the announcement for further information.
