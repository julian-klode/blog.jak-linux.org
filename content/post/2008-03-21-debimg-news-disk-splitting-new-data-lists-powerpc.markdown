---
author: juliank
date: 2008-03-21 19:37:15+00:00
draft: false
title: 'debimg news: disk splitting, new data lists, PowerPC'
type: post
url: /2008/03/21/debimg-news-disk-splitting-new-data-lists-powerpc/
categories:
- Debian
- debimg
---

The next release of debimg (0.0.3) will be the first release supporting splitting packages over multiple disks.  I worked a lot on the base technology today, and the basics are working.

In order to get support for disk splitting, I introduce three new classes: Media, MediaSet and MediaSetCollection (all in libdebimg.media).

The Media class is responsible for adding files to an image (incl. copying/linking), generating extra files (like MD5SUMS or documentation) and for building the image.  It knows the space which is free, the size of each file and the md5sum of each file. It also writes all data inside dists/

The MediaSet class contains one or more Media instances. It has the functionality to split the packages into the disks.

MediaSet knows the dependencies of all packages and tries to add it to the disk with smallest number (e.g. 1) if there is enough space left for the package and all dependencies. If a dependency is on disk2, the package will be added to disk 2 or later. (If one dependency is on the last disk, we don't check where the others are, instead, we put it on the same disk [faster])

The MediaSetCollection class contains multiple MediaSet instances (e.g. for DVDs and CDs), and calls their functions. This makes it possible to build multiple MediaTypes at the same time in an efficient way, because we don't need to call debimg multiple times or run in multiple loops.

This means that many methods of libdebimg.packages.MirrorBuilder move into the new module. For example, the writePackagesFiles() and writeReleaseFiles() will be part of media.Media. (and can be called from MediaSet [for every Media] and MediaSetCollection [for every MediaSet], too)

From boot, run_genisoimage()  will be removed. It is replaced by the createImage() method of media.Media.

In future, debimg will be able to run in three modes: simple, set and sets. The simple mode only creates one disk and is used for netinst and businesscard images. The set is used when only one MediaType has to be generated. The recommended mode for building e.g. weekly-builds is sets, as it has support for multiple MediaTypes.

Another change is the change to the format of data/*.list. I remove the keys called Priority and Tasks. Instead of these, I will add support for these directly into Depends. This means that you will be able to use "Priority:standard" just like "pkgname". This makes sorted lists possible, which are needed for disk splitting. I will also rename the package list to match the names used in debian-cd (mostly) and add a new field called Single-Disk: yes, which disables sorting of the list, and is a bit faster than the other one.

This feature code is unreleased at the moment, but will hopefully be ready next week. Please note that I will never build complete sets with debimg. Therefore, I added a mode to create a list of all packages and build the image without them. (I have no local mirror)

Next week will also be the start of the first daily-builds of PowerPC images and businesscard images available from jak-linux.org/cdimage.

If you want to use the current release (0.0.2), a good point to start is a mail I wrote:

[http://lists.debian.org/debian-cd/2008/03/msg00116.html](http://lists.debian.org/debian-cd/2008/03/msg00116.html)
