---
author: juliank
date: 2010-10-22 16:36:38+00:00
draft: false
title: 'FAIL: Arch Linux switch python executable to Python 3'
type: post
url: /2010/10/22/arch-linux-python-3-and-users/
categories:
- Python
---

Today, I got an email from an user of one of my Python scripts asking why the script t does not work on Arch Linux anymore. As it turns out, the Arch Linux team decided to [switch /usr/bin/python to Python 3.0](http://www.archlinux.org/news/python-is-now-python-3/) and use python2 for Python 2.X versions. By doing this, they decided to make their distribution incompatible to almost any Python script in the world.

Arch Linux's decision to diverge from the rest of the world that uses python for Python 2.X and python3 for Python 3.X is stupid. And doing this without updating reverse dependencies beforehand and thus breaking packages in their own distribution is insane. In the end this means that if you use Arch Linux, you should consider switching to a distribution that does things the right way: Debian. You can also switch to Ubuntu, that's normally just a bit less right (= faster). But using a distribution that does those crazy things in such an irresponsible way is really insane.

Really, how can they be so stupid in the Arch world?
