---
author: juliank
date: 2008-05-06 18:21:54+00:00
draft: false
title: News on debimg
type: post
url: /2008/05/06/debimg-news/
categories:
- Debian
- debimg
---

Well, you may have noticed that debimg 0.1 is still not released. But a lot of work happened over the weekend in my local branch.

First of all, debimg's set support is almost finished. I uploaded a tarball containing the differences between the official lenny weekly build from yesterday and a build created today by debimg, using the tasks of debian-cd 3.0.4 (after manual conversion to a format supported by debimg). Look at [http://jak-linux.org/cdimage/tests/](http://jak-linux.org/cdimage/tests/) for the tarball.

Secondly, the dependency resolver has been rewritten. It's a bit slower now (0.72 seconds for main), but creates much better results. Resolving the dependencies of all packages in Debian Lenny i386 in alphabetical order, debimg 0.0.X resolved 206 dependencies differently than apt. Now, these have been decreased to 15 dependencies, whereas 13 dependencies are false-positive (some packages were not installed because they were already installed). This means that only two ones were different, in this caseachims-guestbook and chdrv, which both depend on virtual-only packages (achims-guestbook: apache | httpd, chdrv: console-utilities).

The third big change is the addition of the hooks module. This module allows you to hook in custom functions, which have access to the Configuration object (ConfigObj) and the MediaSet. There are currently three types of hooks: pre_hooks (run before fetching packages, adding files to the disk), mid_hooks (run after the packages have been fetched) and post_hooks (run after the image has been built). Hooks can be added based on project and architecture, using a simple syntax which support shell patterns. (It's 'project/arch'). The hooks module uses python decorators to register functions. debimg 0.2 will switch to hooks for internal functions, too, like bootloaders and other stuff.

The code has not been merged into the master branch, but I will hopefully be able to merge it tomorrow. The release of debimg 0.1 is now planned for this weekend.
