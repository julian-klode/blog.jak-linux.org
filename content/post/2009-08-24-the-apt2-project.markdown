---
author: juliank
date: 2009-08-24 15:07:45+00:00
draft: false
title: The APT2 project
type: post
url: /2009/08/24/the-apt2-project/
categories:
- APT2
- Debian
---

I just started working on a replacement for APT written in Vala and called APT2 (I know, the name could be better). The main idea behind the project is to create a library for working with Debian repositories and packages, and on top of this library a few applications. This is different from APT because the project focuses on the library part, whereas APT is primarily focused on the application part.

I chose Vala for this task because it has an easy syntax and allows me to use the features provided by GLib and Co. really easily. GLib provides many functions needed for APT like file access, unicode handling, hashsums creation. It also provides us with signals which are useful for implementing progress reporting.

Another project, called 'cupt' tries to provide an APT replacement in Perl. Apart from the fact that I don't like Perl, it also has the disadvantage of being too big to ship on embedded devices and is not useable from other languages such as Python or C/C++. Yet another project, 'smart' provides a different package manager written in Python. While I like Python, it can't be used from languages such as Perl or C/C++ and is too large. APT2 will only require GLib, Gee and libarchive, which require about 2MB of space; about 1/10 of Perl's size.

The core of APT2 is a library called 'libapt'. At the moment, this library provides classes for reading tag files (TagFile&TagSection) and an incomplete configuration class based on libgee's HashMap (to ease coding, it will probably be changed to a special data structure like those in apt-pkg). The next step will be implementing a parser for configuration files (currently we only support in-memory objects) and writing the Acquire system.

The planned Acquire system uses GModule to modularize the support for different URI schemes. Each module provides a worker class which implements one or more URI schemes. The first of these modules will provide a worker using GIO, which deals with local file access, samba shares, FTP, SFTP, WebDAV and various other protocols, including HTTP until a replacement has been written (since we don't want to force gvfs-backends). The workers communicate with the parent Acquire object using signals and can cause the whole acquisition to be aborted by emiting an "abort" signal (or similar).

The whole project has just been started and may take some months until it becomes useful (if it becomes useful at all). The code can be found at [http://git.debian.org/?p=users/jak/apt2.git](http://git.debian.org/?p=users/jak/apt2.git) and is licensed under the MIT license (see [http://www.opensource.org/licenses/mit-license.php](http://www.opensource.org/licenses/mit-license.php)). It is a secondary project and will not affect my work on apt (not much yet) and python-apt (0.8 series).
