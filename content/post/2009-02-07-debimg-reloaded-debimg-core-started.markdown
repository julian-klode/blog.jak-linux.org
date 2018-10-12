---
author: juliank
date: 2009-02-07 19:43:00+00:00
draft: false
title: debimg reloaded - debimg core started
type: post
url: /2009/02/07/debimg-reloaded-debimg-core-started/
categories:
- Debian
- debimg
---

Today, I have published the first pieces of debimg 0.1. The published code includes the resolver, the compression module and the fetcher module. It is rewritten from scratch, this time with a PEP8-conforming style, and more flexible.

Because debimg.core does not depend on any specific configuration format, but is configured solely via parameters, it is more flexible than debimg 0.0. This new code enables people to write their own programs related to Debian images easily. And if you want to, you can use the facilities provided by debimg.configuration and debimg.frontend to write your own program using debimg configuration files (not implemented yet, core needs to be finished first).

Debimg 0.1 will use YAML configuration files, supports multiple repositories, and much more. We could even implement support for pinning packages.

Debimg 0.1 is more than the others. It is a library (actually a python package, debimg.core), it is a program designed for end-users and developers. The enormous flexibility allows us to create applications for almost everyone.

My vision is that someone who needs a custom Debian image simply fires up the debimg GTK+ frontend, selects the packages he/she wants and clicks build. And when someone needs more flexibility, there will be configuration files which lets you configure most aspects. And if this does not suffice, you can write your own application by importing the modules, replacing some functions, methods, etc. and simply call the main() function of the frontend.

**The goals:**



	  * flexibility, high speed, and cool features.
	  * be a show case for the features of the low-level python-apt bindings (apt_pkg, apt_inst)
	  * high-quality code, no hacks, every single function/method/class/module documented.
	  * be a library, and a program.
	  * provide a graphical front-end to assist the unexperienced users.
	  * provide powerful file-based configuration for advanced developers.
	  * And finally, provide a replacement for debian-cd in the near future.

**More:**



	  * Email: [http://lists.debian.org/debian-cd/2009/02/msg00034.html](http://lists.debian.org/debian-cd/2009/02/msg00034.html)
	  * Vcs-Git: git://git.debian.org/users/jak/debimg.git
	  * Vcs-Browser: [http://git.debian.org/?p=users/jak/debimg.git;a=summary](http://git.debian.org/?p=users/jak/debimg.git;a=summary)

