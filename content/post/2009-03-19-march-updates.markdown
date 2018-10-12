---
author: juliank
date: 2009-03-19 19:12:11+00:00
draft: false
title: March updates
type: post
url: /2009/03/19/march-updates/
categories:
- Debian
---

(This is a more or less a TODO list for my Debian packages and other stuff I'm working on)


## Already done




### New package: metatheme-gilouche


Today I uploaded the new package metatheme-gilouche, which builds the binary package gnome-theme-gilouche. The Gilouche theme has been created by openSUSE and is used there as the default theme in GNOME. For users of gnome-app-install, this theme provides a "better" style for your main menu. It contains icons (replacing industrial-icon-theme), GTK+, and Metacity themes. The package is currently NEW, once it is in the archive, I will request removal of industrial-icon-theme. And once this package reaches Ubuntu, Ubuntu's [Bug#96042](https://bugs.launchpad.net/ubuntu/+bug/96042) is closed.


### python-apt


Two weeks ago, Sunday (on 2009-03-08), I coded a bit in python-apt, and introduced a new class apt.package.Version, which contains information about a specific version of a package; and an interface to fetch the source package for that version. You can now simply call something like package.candidate.get_source() to fetch it.

The Package class now provides three new properties: Package.candidate, Package.installed and Package.version. The first two return a Version() object for the candidate/installed version or None, if no one is available (which only happens for installed; because there should always be a candidate [because Package() objects are only created for packages where at least one source is available]). These properties replace those like Package.candidateOrigin, which now is Package.candidate.origins [which also fixes the naming]. The old ones are still available, but accessing them results in a DeprecationWarning.

The whole thing should be hitting unstable soon as 0.7.9.


### Other stuff


Less interesting, but also true - I have uploaded a new version of ndiswrapper (1.54), and the last snapshot of aufs1 (0+20090302-1). I have also renamed the method debimg.core.resolver.Resolver.add_task() to debimg.core.resolver.Resolver.add_tasks(), but this is a really boring change.


## Planned changes




### Planned changes in aufs packaging: switching to aufs2


This is a bit complicated, as aufs2 seems to require a large amount of new exports in the kernel. But we need to switch, because the old version of aufs is not developed anymore upstream. With the switch to aufs2, we will loose functionality like exporting the filesystem via NFS and other ones. The code will be split into two source packages, aufs-utils and aufs.


### Planned changes in gnome-app-install


First of all, I need to merge the new version of gnome-app-install from Ubuntu. Afterwards, I will start working on various packaging related issues. I will switch the package from CDBS to debhelper 7; install the modules to /usr/share/gnome-app-install/, not systemwide; and also try to create a single package which works on Debian and Ubuntu, so we can have a shared package in future.


### Planned changes in command-not-found


First of all, I need to merge the new version from Ubuntu. The version of command-not-found in Debian has various differences from the one shipped by Ubuntu. It uses the files from apt-file to create our command list, it is installed in /usr/share/command-not-found, not /usr/lib/command-not-found, and more.

My plans for the next upload include the inclusion of a pre-generated command-list, for those who do not want to use the apt-file based method; and because it will be available out of the box.


### Planned changes in python-apt


First of all, I am still working on improving the documentation. While everything should be listed already, there are still some problems with their descriptions, and some are missing them. I intent to fix this in python-apt 0.7.10 (or whatever version it will be). Everyone can help, for example by sending new documentation texts or more examples (see [http://apt.alioth.debian.org/python-apt-doc/coding.html](http://apt.alioth.debian.org/python-apt-doc/coding.html) for further information).

Secondly, I will work on a QT4 progress module, in order to equally support GTK+ and QT4 toolkits. This is not really an important task, and if someone else wants to do this, I would be happy too.

Thirdly, I will work on the complete deprecation of mixedCase naming conventions, and switch everything to lowercase_with_underscores; while still providing backward compatibility.

Fourthly, I will complete my work on restructuring the progress module (now a package), to introduce a generic naming scheme, and modules like apt.progress.text who will implement them.


### That's all


If you are a developing for Python, be sure to checkout python2.6 in experimental and thank doko for uploading it. I really hope that python3.1 leaves NEW soon, so I can "play with it".

If you know something else I did or will do in near future, please leave a comment. ;-)
