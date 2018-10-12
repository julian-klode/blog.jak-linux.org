---
author: juliank
date: 2009-01-09 18:00:31+00:00
draft: false
title: 'News from the python-apt front: NEW and COOL DOCUMENTATION'
type: post
url: /2009/01/09/news-from-the-python-apt-front/
categories:
- Debian
- Python
---

I have been working the whole week on python-apt and the result is the jak branch. This implements some of the proposals I made in my last post, but has one very interesting feature: **REAL COOL DOCUMENTATION**.

After **Sandro Tosi** told me in a comment in my last post that the real big problem with python-apt is a lack of documentation, I immediately started writing it. Using**reStructuredText and Sphinx**, we now have a really cool and much more detailed documentation. (Although it is not really finished yet [it contains everything, but there is still room to improve]).

The whole documentation is available at  [http://people.debian.org/~jak/python-apt-doc/](http://people.debian.org/~jak/python-apt-doc/), and the source is in my branch at [http://bzr.debian.org/users/jak/python-apt/jak"](http://bzr.debian.org/users/jak/python-apt/jak), which can be browsed via Loggerhead at: [http://bzr.debian.org/loggerhead/users/jak/python-apt/jak/changes](http://bzr.debian.org/loggerhead/users/jak/python-apt/jak/changes)

It also contains a lot of cleanup, whitespace removal (bundled in one commit), and improved docstrings. And apt.debfile and apt.gtk.widgets should work completely now. Oh, and apt.cdrom now supports sources.list.d.  
