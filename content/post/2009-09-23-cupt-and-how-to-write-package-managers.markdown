---
author: juliank
date: 2009-09-23 11:41:43+00:00
draft: false
title: cupt and how to write package managers
type: post
url: /2009/09/23/cupt-and-how-to-write-package-managers/
categories:
- APT2
- Debian
---

cupt is a new package manager written in Perl by Eugene V. Lyubimkin, who previously contributed to APT. And more than all, the project makes no sense at all.

First of all, there is a language issue. Implementing a package manager in Perl has some major drawbacks. One of the features of APT was it being written in a lower-level language (i.e. C++ which really is below Perl), making it possible to write applications like synaptic and python bindings which in turn lead to applications like gnome-app-install or Ubuntu's new Software Store.

Furthermore, writing a package manager in Perl means that Distributions such as Emdebian might not be able to use it since they have excluded Perl due to its space requirements. This becomes even more important considering that cupt depends on even more perl libraries. This means that cupt will never be able to replace APT.

Secondly, a package manager should not be designed specifically for one distribution. This is another major drawback of cupt and other package managers such as yum or zypper. The smart package manager, written in Python and funded by Canonical Ltd. is an example for a distribution-neutral package manager.

Now let's take a look at package management in modern distributions. Usually we have two levels of package managers, the first being tools like dpkg and rpm which take care of installing and removing the packages and level-2 package managers implementing dependency resolvers and package retrieval from remote locations. Recently, distributions started to add a third layer named PackageKit, which shall provide distribution-independent package management user interfaces. The project was well-received by RPM-based distributions, but failed in Debian-based distributions due to not supporting debconf. Furthermore, adding a third layer just increases the possibility of problems.

The right way to do package management is a distribution-independent level-2 package manager written in C. The smart project shows us that this is possible although itself fails to meet the lower-level language (C) requirement. That's why I decided to write a package manager in Vala, a GObject-based language which gets converted to C and then compiled. If successful, this project will be able to replace most of the current level-2 package managers and will also provide the same distribution-independence as provided by a level-3 package manager such as PackageKit. It is also easy to create binding for other programming language such as Python or Perl thus enabling application developers to choose the language they like most.

The core of this project is a vendor-neutral library, temporarily called libapt (as the project is called APT2 for now). This library contains all the code which is not specific to a vendor i.e. file retrieval, dependency resolver, caches, etc and  is then enhanced by several vendor-specific plugins, each implementing a PackageManager (interface to the distribution's level-1 package manager) and a Repository (well, repositories from which you can download packages) interface.

We could even enhance the vendor-independent interface to include more details of a repository. Most repositories nowadays consist of 4 components: A meta index (Release files for Debian, repomd.xml for Fedora/openSUSE/etc.), a package index (e.g. Packages files for Debian, *primary.xml.gz on Fedora, etc. ), a source index (e.g Sources files in Debian) and a files index (e.g. Contents-*.gz for Debian). I took a look at the repository formats of Slackware, openSUSE and Fedora and it seems that this concept can be applied to all of them. So maybe all we need are distribution dependent parsers for those files.

One of the most important issues with APT is its use of mmap() for the cache. Using mmap() makes it hard to grow the cache, which is sometimes needed. We see a lot of bug reports from people with too small cache sizes. We can circumvent this problem by utilizing an embedded database like SQLite for this, but we would probably loose some speed and it may be harder to maintain a flexible API. We should see what the best option is here, both ways are possible since Vala 0.7.6 includes my patches for adding mmap(), ftruncate(), mremap() and some other functions. An idea to circumvent the mmap() issue is gathering statistics about the relation between the number of repositories and the size of the cache and then using a value which is slightly above the average statistical value.

The project is not very mature yet, it only includes basic library functions for downloading files and parsing configuration files, etc. You can find the (MIT licensed) code at [http://git.debian.org/?p=users/jak/apt2.git](http://git.debian.org/?p=users/jak/apt2.git). I also have some local code for repository management and multi-threaded file fetching, but it's just not ready to be merged yet.
