---
author: juliank
date: 2008-05-22 21:59:42+00:00
draft: false
title: swfdec working perfectly with gstreamer
type: post
url: /2008/05/22/swfdec-working-perfectly-with-gstreamer/
categories:
- Ubuntu
tags:
- gstreamer
- swfdec
---

After the trouble with swfdec and gstreamer, I found out the source of the issue (the fluendo mp3 plugin, see below), and can now use swfdec with gstreamer.

**Warning: Do not use the mp3 plugin from fluendo.com**

swfdec does not always work with the binary mp3 plugin from fluendo.com, at least not in Ubuntu 8.04 64bit. It works with the version shipped in Ubuntu (gstreamer0.10-fluendo-mp3) and with the mad plugin in gstreamer0.10-plugins-ugly. An example is [http://youtube.com/watch?v=CSp7jsV7oG0](http://youtube.com/watch?v=CSp7jsV7oG0)

**Installation of missing gstreamer plugins**

This works on both, Debian and Ubuntu, provided gnome-app-install is installed (default in Ubuntu). Simply open a youtube video, and you will be asked for searching the missing codecs. This also works in almost any other gstreamer application, like rhythmbox or totem.

**Builds of the development branch**

I will provide builds of the 0.7.1 git versions of swfdec and swfdec-mozilla in my PPA soon. This version even supports fullscreen mode in youtube! The PPA will build versions for hardy and intrepid.
