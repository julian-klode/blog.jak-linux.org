---
author: juliank
date: 2011-04-15 13:15:02+00:00
draft: false
title: 'this week: apt 0.8.14 (regex pinning), stable updates, and bug triaging'
type: post
url: /2011/04/15/this-week-apt-0-8-14-regex-pinning-stable-updates-and-bug-triaging/
categories:
- Debian
---

### python-apt 0.8.0~exp2 bug fix release


On Tuesday, I uploaded python-apt 0.8.0~exp2 to experimental, fixing about 10 bugs reported in Ubuntu and Debian bug trackers. It should know even convert integers correctly on all architectures, previously we could have passed long via varargs where int was expected.



### Bugs


Until Thursday, I went through the bug list in Launchpad and closed/fixed/reassigned/merged about 100 bugs in APT and python-apt.



### APT & python-apt updates for squeeze


Today, I uploaded updates of apt and python-apt to stable. They include support for xz and parsing multi-arch dependencies, as wanted by ftpmasters.



### APT 0.8.14 and wildcards/regular expression pinning


Today, I uploaded apt 0.8.14 to Debian unstable, introducing support for pinning using glob() like Syntax and POSIX extended regular expressions. Let's say we want to pin all packages starting with gnome or kde to 990. The following example does this, using glob-like patterns for gnome, and a regular expression enclosed in / for kde:
`
Package: gnome* /^kde/
Pin: release a=experimental
Pin-Priority: 990
`

This closes 10-year-old [Bug#121132](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=121132) in Debian. Have fun with this feature, but please note that it may not be the fastest thing on earth, as it checks every package in the cache on initialization of such queries, which may take a few 10 ms.

Since some time already, it's also possible to use such expressions for the Pin field. Thus users of Ubuntu releases could use the following piece of preferences to pin all packages in archives starting with lucid (e.g. lucid, lucid-updates) to 990:
`
Package: *
Pin: release a=lucid*
Pin-Priority: 990
`

Those types of pins do not have the negative performance impact of complex expressions in the Package header, as they are only checked against a smaller set of packages, or if "Package: *", simply checked against the package files in the cache.
