---
author: juliank
date: 2008-02-25 20:41:10+00:00
draft: false
title: debimg - debian-cd in Python
type: post
url: /2008/02/25/debimg-debian-cd-in-python/
categories:
- Debian
- debimg
---

I'm currently working on a rewrite of debian-cd in Python. Although there is already deb-imgs-gen, I decided to start from scratch, because deb-imgs-gen is more than 1 year old.

debimg's main features are


### Speed


debimg should be able to build netinst disks in less than 20 seconds


### Free Software


This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.


### Easy Configuration





	  * Packages can be included based on their priority, tasks or name (no manually created task files)
	  * All packages are defined in one file,which is based on the format on debian/control. You can even use the "package [architectures]" syntax from Build-Depends



### Based on python-apt





	  * Highspeed dependency solver written in C (or C++ ?)
	  * Used for downloading all kind of data in debimg
	  * Packages{,.gz} files are created from the apt cache instead of scanning the disk



many features are missing at the moment, and no code has been released. I will send an email containing more details, like configuration file examples, to the MLs in a few days.




[debimg homepage at jak-linux.org](http://jak-linux.org/projects/debimg/)
