---
author: juliank
date: 2009-11-03 17:51:34+00:00
draft: false
title: My First upload with new source format
type: post
url: /2009/11/03/my-first-upload-with-new-source-format/
categories:
- Debian
- Ubuntu
---

Yesterday, I uploaded command-not-found 0.2.38-1 (based on version 0.2.38ubuntu4) to Debian unstable, using the "3.0 (quilt)" source format. All steps worked perfectly, including stuff like cowbuilder, lintian, debdiff, dput and the processing on ftp-master. Next steps are reverting my machine from Ubuntu 9.10 to my Debian unstable system and uploading new versions of gnome-main-menu, python-apt (0.7.93, not finished yet) and some other packages.

In other news, the development of Ubuntu 10.04 Lucid Lynx just started. For the first time in Ubuntu's history, the development will be based on the testing tree of Debian and not on the unstable tree. This is done in order to increase the stability of the distribution, as this release is going to be a long term supported release. Ubuntu will freeze in February, one month before the freeze of Debian Squeeze. This should give us enough room to collaborate, especially on bugfixes. This also means that I will freeze my packages in February, so they will have the same version in Squeeze and Lucid (applying the earliest freeze to both distributions; exceptions where needed).
