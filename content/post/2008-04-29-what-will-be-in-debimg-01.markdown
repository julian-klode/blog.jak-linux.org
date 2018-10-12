---
author: juliank
date: 2008-04-29 19:14:03+00:00
draft: false
title: What will be in debimg 0.1
type: post
url: /2008/04/29/what-will-be-in-debimg-01/
categories:
- Debian
- debimg
---

debimg 0.1 will be the first major milestone in the development of debimg. I will now list some changes compared to the current release, debimg 0.0.3 (_Please note that the following text is from an internal NEWS file and may not be correct in some aspects, as it is already some days old_)


#### Support for disk splitting


This release of debimg adds support for creating media sets, i.e. splitting the packages over multiple disks. This is achieved by providing a new class called MediaSet, which passes all calls to methods to all medias.

When a package is added to a MediaSet, MediaSet tries to find the first disk where it can be added, by checking if all dependencies of the package are provided on the disk (or previous ones). This dependency checker does no recursive dependency checks, and can be disabled via OptimizedDiskSplitting = False (or no, n, 0...) in the configuration file.

The MediaSet classes are also lists, so you can access disk one via the index 0. BaseMedia has been modified to also support being accessed via index, using disknumber-1 in order to have both classes share the same API.


#### New data lists


This release of debimg brings users a more powerful way to include packages. Instead of various keys to include packages, debimg now uses the Include key.

To include packages, you have to use the 'Include' field. The value is a list of items, separated by commas. An item may either be the name of a package or a special form written as key:value. In this case, the following keys are supported:



Task/Priority:
This includes all packages belonging to the specified task or priority. In
case of tasks, debimg first includes all Key packages, then the other
packages.





#### Configuration files are easier


This release of debimg makes it possible to build multiple architectures using the Architectures option. This option replaces the previous Architecture option, which is now set automatically by the script for each architecture.

It also enables the Projects option, in case you want to build multiple projects. (All need to have the same MediaType and same NumberOfDisks). The project may also be cd-set, dvd-set, dvd9-set, netinst or businesscard. In these cases, MediaType is set automatically. [MediaType may also be moved in to data files].

This release also allows you to prefix any configuration value with path: in order to automatically convert the value to an absolute path. This is needed for many file options, but should not be used for some other stuff.


#### Improved Jigdo Support


debimg 0.1 allows you to define the public path (name) to (of) the image file and the template file that is written to the Jigdo file.


#### Use urlgrabber for file downloading


Starting with this release, debimg uses urlgrabber to download all kinds of files (except packages). A urlgrab call has been added to BaseMedia.addFile() which now understands http:// and ftp:// urls.


#### Plugins (maybe)


debimg 0.1 may introduce support for registering custom functions. This feature is low-priority, although required for easy development of Ubuntu-related code.


#### About debimg


debimg is a GPL-3 licensed software designed to replace debian-cd, a tool to create Debian images. For further information about debimg, visit the [Wiki page](http://wiki.debian.org/DebImg). For more information about Debian, visit the website at [www.debian.org](http://www.debian.org/).
