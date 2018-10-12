---
author: juliank
date: 2009-04-15 18:35:57+00:00
draft: false
title: python-apt to become first Debian package to support Python 3
type: post
url: /2009/04/15/python-apt-to-become-first-debian-package-to-support-python-3/
categories:
- Debian
---

Python 3.1 is still in experimental, but python-apt already has a fully working Python 3 version. With the patch being available in the 'jak' branch, python-apt [Bug#523645](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=523645) can be closed soon.

And this is not the only change. Memory usage has been decreased by 10MB by creating the Package() objects on the fly instead of pre-creating all 25000 ones. All classes which previously supported the has_key() method now support __contains__, which allows you to write 'key in mapping'.

But that's not all. The Package class now gained support for setting the candidate version of a package, in the same way you get it, using the property: `mypkg.candidate = max(mypkg.versions)`. And you can now pass file descriptors to functions previously only working with file() objects.

But we're not done yet. The complete API change is pending, renaming everything to PEP-8 compliant names and deprecating the old ones, which will be removed at a later time (after the release of Squeeze). The module `apt.debfile` is not affected by this change, because it already used the correct names. But for Python 3, we will not keep backward compatibility, in order to make coding easier and to make it clear that applications should be ported to the new API.

And if you want to get your feature into python-apt now is your time. If you want something merged, provide the code, the documentation (with example) and a list of use cases; and report a wishlist bug in the Debian BTS.

And if you want to write a tutorial about python-apt, write it in reStructuredText and I will add it to the documentation. The documentation is currently basically an API reference and there could be much more text.

Python-apt 0.7.90 is currently uploading. The whole development will result in python-apt 0.8.
