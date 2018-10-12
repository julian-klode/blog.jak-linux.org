---
author: juliank
date: 2009-03-01 19:02:32+00:00
draft: false
title: debimg update - creating images
type: post
url: /2009/03/01/debimg-update-creating-images/
categories:
- Debian
- debimg
- Ubuntu
---

Much happened since the last time  I wrote about debimg. The project is now registered on Alioth and has a mailing list. On the code side, there have also been several changes.

First of all, the repository module has been merged into the master branch. This was the first step towards the creation of the image building, which happened today by introducing the 'image' module.

The code should be treated as Beta quality, but the project as a whole is Alpha, because the application utilizing debimg.core is still missing. As always, I hereby encourage to try out debimg, have a look at the examples, and help to develop it.

Patches should be sent to the mailing list, created with git format-patch, and its usual settings (eg. prefixed with eg. '[PATCH 1/2]'). The patches should be inline and validate in pyflakes and using pep8.py. See the [README](http://git.debian.org/?p=debimg/debimg.git;a=blob_plain;f=README;hb=HEAD) for some more recommendations.

Because NEW seems to be really busy at the moment (and doko uploaded python2.6 and python3.1), I'm not uploading the current state as 0.1.0~a1 to experimental, but wait until NEW is smaller (maybe it will be 0.1.0~b1 then).


## What is wanted/planned?





	  * Compatibility configuration formats

	    * (debimg.config.simple_cdd) A reimplementation of simple-cdd using debimg. This probably needs to wait until there is a module for dealing with the installer, but I want to implement an application to support simple-cdd configuration files.
	    * (debimg.config.debian_cd) There could be an implementation of debian-cd's configuration format. This would allow people to easily try out debimg. We can only support a subset, though.


	  * New configuration formats

	    * (debimg.config.yaml) Debimg's native configuration format. This is the only one supported by the graphical frontends. Where possible, configuration between compatibility formats and this format will be provided.


	  * Graphical Frontends:

	    * (debimg.frontend.gtk2) The graphical GTK+ frontend for inexperienced users who just want to create their own disk.
	    * (debimg.frontend.qt4) The graphical frontend written in QT4.


	  * Text frontends

	    * (debimg.frontend.text) The basic command-line frontend.
	    * (debimg.ubuntu.frontend.text) A script to build Ubuntu images, which could be used to build the official Ubuntu Images. This requires interaction with the germinate tool for dependency resolution, and more. It's also not flexible enough for building custom images.





## Requirements for 0.1 Beta





	  * Implement at least one configuration format and the build frontend.
	  * Have at least one external contributor.



## More





	  * Mailing-List: [debimg-devel@lists.alioth.debian.org ](mailto:debimg-devel@lists.alioth.debian.org) (Archive at [http://lists.alioth.debian.org/pipermail/debimg-devel/](http://lists.alioth.debian.org/pipermail/debimg-devel/))
	  * Wiki: [http://wiki.debian.org/DebImg](http://wiki.debian.org/DebImg)
	  * VCS-Git: git://git.debian.org/debimg/debimg.git
	  * VCS-Browser: [http://git.debian.org/?p=debimg/debimg.git](http://git.debian.org/?p=debimg/debimg.git)



## Changes


Julian Andres Klode (6):



	  * debimg/core/files: When creating a file object allow filename as source
	  * debimg/core/resolver.py: Introduce Package.fullname, Package.component
	  * debimg/core/repository.py: Merge the repository module.
	  * debimg/core/resolver.py: Improve handling of certain dependency types
	  * debimg/core/repository.py: Allow Repository.add_group to take a 'distro' parameter
	  * debimg/core/image.py: Introduce the image module.

