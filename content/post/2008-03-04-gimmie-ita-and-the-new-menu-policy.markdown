---
author: juliank
date: 2008-03-04 22:36:23+00:00
draft: false
title: gimmie (ITA) and the new menu policy + building with pristine-tar
type: post
url: /2008/03/04/gimmie-ita-and-the-new-menu-policy/
categories:
- Debian
---

While working on [Bug#460620: ITA: gimmie -- elegant desktop organizer](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=460620), I noticed that I need to upgrade debian/menu to the new policy.

Currently, gimmie uses  Apps/Tools, but what should I use now? It does not fit into the other sections. Recommendations?

Other important changes:



	  * I am the new maintainer
	  * Gmenu and sexy extensions are not built, instead the python-gmenu and python-sexy packages are used
	  * Gimmie's extensions are compiled for Python 2.4 and Python 2.5
	  * debian/copyright uses the format defined at [http://wiki.debian.org/Proposals/CopyrightFormat](http://wiki.debian.org/Proposals/CopyrightFormat)
	  * The suspend and hibernations buttons are back again ([Commit](http://git.debian.org/?p=collab-maint/gimmie.git;a=commit;h=485f334993753f9afb98ed11e686abbe08abff36))

The package is maintained in a git repo in the collab-maint project, and can be viewed online using [Gitweb](http://git.debian.org/?p=collab-maint/gimmie.git;a=summary). You can get the source from its repo at [git://git.debian.org/git/collab-maint/gimmie.git](//git.debian.org/git/collab-maint/gimmie.git)

To create the orig.tar.gz tarballs, you need to have pristine-tar installed. To build the package, install git-buildpackage (from unstable) and pristine-tar and simply run 'git-buildpackage --git-pristine-tar'

The same instructions also apply to building readahead-list, which can be found at [git://git.debian.org/git/collab-maint/readahead-list.git](//git.debian.org/git/collab-maint/readahead-list.git)
