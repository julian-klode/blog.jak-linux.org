---
author: juliank
date: 2009-04-01 16:15:29+00:00
draft: false
title: python-apt 0.7.10 released
type: post
url: /2009/04/01/python-apt-0710-released/
categories:
- Debian
---

I have just uploaded a version of python-apt 0.7.10 to unstable ( my first upload of python-apt, all previous uploads were done by Michael Vogt).

This release is mainly a bugfix release, but also brings new features like apt.package.Version.uri and apt.package.Version.fetch_binary().I also added a Breaks: debdelta (<< 0.28~) because debdelta 0.27 is not working anymore since python-apt 0.7.9 and I expect that this problem will be fixed in 0.28, which could then use the new apt.package.Version.uri API to fetch the uris of the packages).

Here is the changelog:

python-apt (0.7.10) unstable; urgency=low



	  * Build-Depend on python-debian, use it to get version number from changelog
	  * Depend on libjs-jquery, and remove internal copy (Closes: #521532)
	  * apt/package.py:

	    *  Introduce Version.{uri,uris,fetch_binary()}


	  * debian/control:

	    * Remove mdz from Uploaders (Closes: #521477), add myself.
	    * Update Standards-Version to 3.8.1
	    * Use ${binary:Version} instead of ${Source-Version}
	    * Fix spelling error: python -> Python


	  * debian/copyright: Switch to machine-interpretable copyright
	  * Fix documentation building

	    * doc/source/conf.py: Only include directories for current python version.
	    * debian/control: Build-Depend on python-gtk2, python-vte.
	    * setup.py: If pygtk can not be imported, do not build the documentation.


	  * Breaks: debdelta (<< 0.28~) to avoid more problems due to the internal API changes from 0.7.9.


-- Julian Andres Klode <jak@debian.org>  Wed, 01 Apr 2009 15:24:29 +0200


Have fun.
