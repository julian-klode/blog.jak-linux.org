---
author: juliank
date: 2008-04-04 19:00:12+00:00
draft: false
title: debimg 0.0.3 - "the checksum" - released
type: post
url: /2008/04/04/debimg-003-released/
categories:
- Debian
- debimg
---

Dear readers,

The third release of debimg is available now: 0.0.3

Get the tarball: [http://alioth.debian.org/~jak-guest/debimg_0.0.3.tar.gz](http://alioth.debian.org/~jak-guest/debimg_0.0.3.tar.gz)
Verify it:       [http://alioth.debian.org/~jak-guest/debimg_0.0.3.tar.gz.asc](http://alioth.debian.org/~jak-guest/debimg_0.0.3.tar.gz.asc)
The ChangeLog:   [http://alioth.debian.org/~jak-guest/ChangeLog-0.0.3](http://alioth.debian.org/~jak-guest/ChangeLog-0.0.3)

Clone git repo: git://git.debian.org/git/users/jak-guest/debimg.git
Browse the repo: [http://git.debian.org/?p=users/jak-guest/debimg.git](http://git.debian.org/?p=users/jak-guest/debimg.git)

More Information: [http://wiki.debian.org/DebImg](http://wiki.debian.org/DebImg)
Daily images:     [http://jak-linux.org/cdimage/daily-builds/testing/](http://jak-linux.org/cdimage/daily-builds/testing/)


#### About debimg


debimg is a software designed to replace debian-cd, written in Python, and
supporting the creation of single disks for the i386 and amd64 architectures.

debimg is of course free software and licensed under the terms of the GNU
General Public License 3 or (at your option) any later version.


#### About "the checksum"


This release is called "the checksum", because the software knows
the MD5SUM, SHA1SUM and SHA256SUM of every file on the disk.


#### News





	  * Introduction of the media module

	    * Add md5sum.txt and sha1sum.txt to the image
	    * NEW OPTION: JigdoMap, see the config file
	    * Lot of code cleanup


	  * Support for custom installer images

	    * Modify InstallerImages to an url supported by apt


	  * Renamed most options in the configuration file for better
readability
	  * debimg requires Python 2.5, as it uses the with statement.



#### Description of the Release


This release of debimg introduces the media module with its classes
MediaFile, BaseMedia and DebianMedia.

The MediaFile class contains information about a file.
It contains the absolute path to the file on the filesystem,
the path on the media, its size, md5sum, sha1sum and sha256sum.

The BaseMedia class provides methods to add files to the
image, open files on it, and creating the final image. It also
provides methods to create the files md5sum.txt and sha1sum.txt,
and methods to support Jigdo file creation.

The DebianMedia class provides methods to add packages to
the image, creating Release and Packages files for dists.


#### Quick start


To get started with debimg, get the tarball and extract it to
some directory.

Now, open the file debimg.cfg and change the option Mirror to the URL
of your preferred mirror. This mirror may be any kind of mirror supported by
apt, but if you use file:/ they have to be on the same mountpoint, as the files
are hardlinked. (use copy:/ to get them copied).

Now, run `./debimg debimg.cfg`. This will create an ISO image named
debian-lenny-i386-netinst.iso. This image is a normal netinst (except for
missing documentation and some other small things), and contains the Lenny d-i.

To change more settings, take a look at debimg.cfg.


#### Future





	  * Cleanup of the configuration format (almost finished)
	  * Support for splitting disks

	    * Introduction of MediaSet class
	    * Changes to the lists required


	  * Add documentation to the disks
	  * Support for PowerPC
	  * Create Debian package (almost finished)

Another interesting feature will be the libisofs [0] support provided by
the python-libisofs extension, which is currently under development. [1]


#### Previous release announcements





	  * 0.0.2: [http://lists.debian.org/debian-cd/2008/03/msg00114.html](http://lists.debian.org/debian-cd/2008/03/msg00114.html)
	  * 0.0.1: [http://lists.debian.org/debian-cd/2008/03/msg00021.html](http://lists.debian.org/debian-cd/2008/03/msg00021.html)



#### Links





	  * [0] libburnia project: [http://libburnia-project.org/](http://libburnia-project.org/)
	  * [1] [http://juliank.wordpress.com/2008/04/02/python-extension-for-libisofs/](http://juliank.wordpress.com/2008/04/02/python-extension-for-libisofs/)

