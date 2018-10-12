---
author: juliank
date: 2008-02-11 16:39:28+00:00
draft: false
title: JAK LINUX website now powered by ikiwiki
type: post
url: /2008/02/11/jak-linux-website-now-powered-by-ikiwiki/
categories:
- General
---

I'm glad to announce that finally, after being powered by ftpsync for more than six months,  the [JAK LINUX website](http://jak-linux.org/) now uses [ikiwiki](http://ikiwiki.info/).

I currently have some small issues with the website: After using --rebuild, tarballs have a different modification time and are therefore reuploaded everytime, though the content is actually the same. I would also need a plugin to create directory indexes with sha1sums, but I haven't found one yet. (If you know one, please let me know).

If you have never heard of ikiwiki: ikiwiki is a wiki system used and developed by Debian Developer Joey Hess and many contributors. In contrast to ftpsync, a python script I wrote in 2007, it has an active upstream with multiple contributors, and supports multiple markup languages (e.g. Markdown).

This switch to ikiwiki is also a switch back to the design used at mentors.debian.net, which had been replaced in December 2007 with a (CC-licensed) design created by styleshout.com. This template just looks better and has the better license (GPL-2).

In the next days, I will cleanup and extend the website and the template and release both under the terms of the GNU GPL version 2. I will alsoI will also try to write a plugin for directory indexes,  write a plugin to create directory indexes (although I have almost no experience with perl), and will release it under the GPL 2.

Thank you, Joey and all contributors for creating this software.
