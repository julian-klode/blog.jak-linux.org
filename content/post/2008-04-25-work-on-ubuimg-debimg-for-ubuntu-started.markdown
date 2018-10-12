---
author: juliank
date: 2008-04-25 14:28:34+00:00
draft: false
title: Work on ubuimg / debimg for Ubuntu started
type: post
url: /2008/04/25/work-on-ubuimg-debimg-for-ubuntu-started/
categories:
- debimg
- Ubuntu
---

The work on the Ubuntu version of debimg has begun. The majority of changes will be the following ones (in the order they will be done):



	  1. Change debimg to use germinate to calculate dependencies (package lists)
	  2. Add the additional stuff (live, etc.)

Once we can recreate the Ubuntu hardy i386 and amd64 alternate disks, work starts on the live filesystem and on merging these features back into debimg master, which will also get support for more archs.

debimg uses germinate directly on the Python level.

debimg 0.0.3ubuntu1 is sheduled for this Sunday. This will be more or less really hacks.

	  * [master] Move the fetching of packages from packages to media, so we can use it for all files
	  * Add libdebimg.germinate as a wrapper around germinate, providing functions to build the disks
	  * Modify libdebimg to build all disks in one run, multiple architectures and multiple seeds.

The basic code structure will look like the following:

	  1. For each architecture:

	    1. seeds = Run germinate
	    2. For seed in seeds:

	      1. Get the packages
	      2. Get extra files
	      3. Build the disk





The Debian version may switch to seed files too, in version 0.2.
