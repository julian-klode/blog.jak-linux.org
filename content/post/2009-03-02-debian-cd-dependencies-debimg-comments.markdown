---
author: juliank
date: 2009-03-02 16:54:40+00:00
draft: false
title: debian-cd, dependencies, debimg, comments
type: post
url: /2009/03/02/debian-cd-dependencies-debimg-comments/
categories:
- Debian
- debimg
---

Looking at the amd64 CD images of Lenny, I just saw that there is the package 'gnome' on disk 1, while some of its dependencies are on disk 2. I don't think that this is good. Same also applies to K3B on disk 3, and openoffice.org-kde on KDE-disk 1.

In my opinion, all packages which are located on a disk X, should only depend on a disk N (N<X). This means that the package gnome would be moved to disk 2, or its dependencies to disk 1.

This is exactly the way debimg works. Debimg uses so-called package groups, which simply represents a set of packages with cyclic dependencies. These package groups are returned in a specific order, so that a group N only requires a group <N. This order is kept when the groups are added to the disk. Furthermore, we treat the groups as one when adding them to the disk, ie. we check whether the whole group fits on the disk (and add it) or not (create a new disk). This way, we ensure that all dependencies can be satisfied.

Today, I decided to try it out and therefore wrote a small script reading the debian-cd task files and comparing the file list (of the packages added to the disk) with the file list of the official KDE disk.

The results look very good, debimg adds 11 packages and removes 26 which is not that much, and mostly caused by wrong size limits, etc. You can look at the results your self, and regenerate them using:



	  * [http://debimg.alioth.debian.org/tests/debian-500-amd64-kde-CD-1.diff](http://debimg.alioth.debian.org/tests/debian-500-amd64-kde-CD-1.diff) - The results
	  * [http://debimg.alioth.debian.org/tests/debian-cd.py](http://debimg.alioth.debian.org/tests/debian-cd.py) - The script used.
	  * [http://debimg.alioth.debian.org/tests/debimg.tar.gz](http://debimg.alioth.debian.org/tests/debimg.tar.gz) - The version of debimg used (current HEAD)

Anyway, debimg still needs real configuration and handling of the debian installer and source packages, but this should give you an idea of how debimg works. And a tarball, for those who don't want to use git all the time.

BTW, I have now enabled comment threading here, a [new Wordpress feature](http://en.blog.wordpress.com/2009/02/19/comment-threading-is-here-plus-other-cool-comment-settings/). I hope that it works, as I have not tried it out yet.
