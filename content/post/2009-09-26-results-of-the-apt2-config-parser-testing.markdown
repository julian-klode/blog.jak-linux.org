---
author: juliank
date: 2009-09-26 18:12:09+00:00
draft: false
title: Results of the APT2 config parser testing
type: post
url: /2009/09/26/results-of-the-apt2-config-parser-testing/
categories:
- APT2
---

Thanks to those who have tested it (and/or will test it). The results where helpful and resulted in [Bug#548443](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=548443) filed against localepurge and [GNOME Bug #596429](https://bugzilla.gnome.org/show_bug.cgi?id=596429) against glib. The first one is a case where quotes where used inside a value, although this has never been defined to work, and the second one is a problem with GLib's GScanner not ignoring multi-line C-style comments although it was configured to do so.

I also fixed some bugs in APT2, like the missing build-depends on libgee-dev and the configuration parser now accepts '.', '_', '+' in the option name. I also talked with Eugene about some differences in the way cupt and APT2 handle quotes and about some other parts of the configuration format. Seems this was a good day.
