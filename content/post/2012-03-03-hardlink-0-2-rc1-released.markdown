---
author: juliank
date: 2012-03-03 18:39:55+00:00
draft: false
title: hardlink 0.2 RC1 released
type: post
url: /2012/03/03/hardlink-0-2-rc1-released/
categories:
- General
---

I have just released version 0.2 RC1 of my hardlink program. Compared to the 0.1.X series, the program has been rewritten in C, as Python was to memory-hungry for people with millions of files. The new program uses almost the same algorithm and has almost completely the same bugs as the old version.

The code should be portable to all UNIX-like platforms supporting nftw(). I have tested the code on Debian, FreeBSD 9, and Minix 3.2. For storing path names, it uses a flexible array member on C99 compilers, a zero-length-array on GNU compilers, and a array of length 1 on all other compilers (which should work everywhere as far as I heard).

The new version may have slightly different behaviour compared to 0.1.2 when regular expressions are specified on the command-line, as a result of the switch from Python's regular expression engine to PCRE (if compiled with PCRE support, you can also use POSIX extended regular expressions if you like).

The code is significantly faster than the old code (in situations where it's not I/O bound), and uses much less memory than the old one. Per file, we now store a <tt>struct stat</tt>, a pointer, an int, a char, and the filename; as well as three pointers for a binary search tree (which uses tsearch()).

It should also be compatible to Red Hat's original hardlink tool now command-line-wise, there is at least a -c option now. The history and the name conflict are interesting, but probably nothing for this post. We're even less resistant against changing trees than Fedora's tool (and derived) currently, but should otherwise be better (and far more complicated and feature-packed). And we don't require mmap(), but use fread() instead. There was no real performance difference in testing. And we are not GPL-licensed, but use the MIT/Expat license.

The package is currently entering Debian experimental for testing purposes. If you have used hardlink previously, or are just curious, give it try.

And the makefile is now compatible with the various BSD makes out there, if that's interesting for you.

Link to website: [http://jak-linux.org/projects/hardlink/](http://jak-linux.org/projects/hardlink/)
