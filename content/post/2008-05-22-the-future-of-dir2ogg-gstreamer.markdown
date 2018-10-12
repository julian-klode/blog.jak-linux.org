---
author: juliank
date: 2008-05-22 22:23:03+00:00
draft: false
title: The future of dir2ogg - gstreamer?
type: post
url: /2008/05/23/the-future-of-dir2ogg-gstreamer/
categories:
- General
tags:
- dir2ogg
- gstreamer
---

After playing a bit with gst-launch, I found out that it can convert music files and keeps the tags. Therefore, I think it would be great to rewrite dir2ogg using gstreamer (the python bindings).

This version of dir2ogg will be much much smaller, and is really easy to extend. It will also support multiple output formats and does not need to know about the input files (use -i 'SHELL PATTERN' to include other files).

But it will not really replace dir2ogg. The old dir2ogg will still be supported.
