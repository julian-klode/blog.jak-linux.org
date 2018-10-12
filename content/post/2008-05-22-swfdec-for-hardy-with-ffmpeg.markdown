---
author: juliank
date: 2008-05-22 19:02:20+00:00
draft: false
title: 'Ubuntu: swfdec using ffmpeg in PPA'
type: post
url: /2008/05/22/swfdec-for-hardy-with-ffmpeg/
categories:
- Ubuntu
tags:
- swfdec
---

I created a version of swfdec 0.6.6 using mad and ffmpeg instead of gstreamer, because with gstreamer it failed to play multiple videos on youtube.com.

The release is available in my PPA at:

    
    deb http://ppa.launchpad.net/juliank/ubuntu hardy main
    deb-src http://ppa.launchpad.net/juliank/ubuntu hardy main



I will also provide some builds of the development branch (0.7.1) soon.

**Update:**Maybe it was not clear, but the videos crashed the browser. It also didn't really work in totem and I'm still looking for the source of the problem. I have every available gstreamer plugin package installed. Try it yourself, [http://de.youtube.com/watch?v=CSp7jsV7oG0](http://youtube.com/watch?v=CSp7jsV7oG0). It works with gnash, but gnash does not work with wordpress stats page.

**Update 2:** I now found the real problem: I had an binary version of fluendo's mp3 plugin installed (from fluendo.com), which caused the crash. After removing the file, everything works. (using fluendo-mp3 shipped with Ubuntu).

**Update 3:** I removed the ffmpeg version from my PPA, as it is not needed.
