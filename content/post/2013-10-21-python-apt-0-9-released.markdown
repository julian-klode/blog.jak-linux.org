---
author: juliank
date: 2013-10-21 22:03:58+00:00
draft: false
title: python-apt 0.9 released
type: post
url: /2013/10/22/python-apt-0-9-released/
categories:
- Debian
---

I released python-apt 0.9. This completely removes support for the old API from the code base (it was disabled for the entirety of 0.8 in Debian, and in Ubuntu since saucy). Highlights:  * Cleanup: Complete removal of old-api support code  * Bug fix: Various coverty bug fixes by Michael Vogt  * Bug fix: Correctly handles multi-arch dependencies in apt.debfile, so packagekit and gdebi can now install local multi-arch packages correctly  * Bug fix: A segmentation fault has been fixed. When releasing the value of the policy attribute of an apt_pkg.Cache object, its destructor deleted the pkgPolicy, but that was managed by a CacheFile from APT, causing it to be deleted twice.  * Bug fix: Tests do not depend on the contents of /tmp anymore  * Bug fix: All examples and old tests have been updated to the current python-apt API  * Feature: Paths can now be specified using 'bytes' objects instead of 'str' in Python 3.  * Ubuntu-specific: Meta-data for Ubuntu 14.04 -- although with a typo ('thar' instead of 'tahr'), but that is fixed in git

 
