---
author: juliank
date: 2013-04-09 18:40:16+00:00
draft: false
title: apt-show-versions rewrite in C++ (more than 10 times faster)
type: post
url: /2013/04/09/apt-show-versions-rewrite-in-c-more-than-100-times-faster/
categories:
- Debian
---

The script apt-show-versions is developed by another Debian Developer called Christoph Martin in Perl. Recently, it turned out that apt-show-versions is too slow for some users; so I decided to rewrite his program using APT's C++ API. I expect this to be part of a future APT release, rendering the original apt-show-versions obsolete.

The rewrite is sadly not 100% backwards compatible to the original version; as some option names had to be renamed due to our command-line parser not supporting option names like -nh, and some other options were dropped because they are hard to support (like --status-file and --lists-dir) with our command-line parsing. I also decided not to keep the the -p and -r options, but use the standard APT command-line conventions insteads.

For now, it also cannot show you the distribution names you have specified in your sources.list file, but will always display codenames instead; if available. I hope to fix this in Jessie by extending APT's cache format a bit.

On the performance side, this program now takes about 0.09s compared to the 1.40 seconds needed by apt-show-versions. The times are taken with all data in caches.

The current version can be found in a git repository, a link to gitweb is:

[http://anonscm.debian.org/gitweb/?p=users/jak/apt-show-versions.git
](http://anonscm.debian.org/gitweb/?p=users/jak/apt-show-versions.git)

Please also note that support for --allversions is not 100% implemented yet, but it should work for most uses.

Now, go testing and report back!
