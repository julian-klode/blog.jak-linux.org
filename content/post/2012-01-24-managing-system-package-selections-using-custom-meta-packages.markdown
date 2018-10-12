---
author: juliank
date: 2012-01-24 09:43:05+00:00
draft: false
title: Managing system package selections using custom meta packages
type: post
url: /2012/01/24/managing-system-package-selections-using-custom-meta-packages/
categories:
- Debian
- General
tags:
- meta package
---

Over the last years, I have developed a variety of metapackages for managing the package selections of the systems I administrate. The meta packages are organized like this:




jak-standard

    Standard packages for all systems

jak-desktop

    Standard packages for all desktop systems (GNOME 3 if possible, otherwise GNOME 2)

jak-printing

    Print support

jak-devel

    Development packages

jak-machine-<X>

    The meta package defining the computer X



Each computer has a jak-machine-X package installed. This package is marked as manually installed, all other packages are marked as automatically installed. 

The machine packages have the attribute `XB-Important: yes` set in debian/control. This creates an `Important: yes` field. This field is not official, but APT recognizes it and does not remove those packages (the same field is set for the APT package by APT when building the cache, as APT should not be removed either by APT). It seems to work a bit like `Essential`, with the exception that non-installed packages are not installed automatically on `dist-upgrade`.

The meta packages are created using seed files similar to Ubuntu. In contrast to Ubuntu, I'm not using `germinate` to create the packages from the seeds, but a custom `dh_germinate_lite` that simply takes a seed file and creates the correct substvars. It's faster than germinate and really simplistic. It also does not handle Recommends currently.

The whole result can be seen on [http://anonscm.debian.org/gitweb/?p=users/jak/jak-meta.git](http://anonscm.debian.org/gitweb/?p=users/jak/jak-meta.git). Maybe that's useful for some people. And if you happen to find some packages in the seeds that are deprecated, please let me know. Oh, and yes, some packages (such as the letterman one) are internal software not publically available yet [letterman is a simple GUI for creating letters using LaTeX].

While I'm at it, I also built Ubuntu's version of wine1.2 for i386 squeeze. It can be found in
`deb [http://people.debian.org/~jak/debian/](http://people.debian.org/~jak/debian/) squeeze main` (it still needs a few changes to be correct though, I'll upload a jak2 build soon). I also built updated sun-java6 packages for my parents (mostly needed due to the plugin, some websites do not work with the IcedTea one), but can't share the binaries due to licensing requirements. I may push out a source repository, though, so others can build those packages themselves. I'll let you know once that's done.
