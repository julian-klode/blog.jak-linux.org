---
author: juliank
date: 2008-10-10 15:23:15+00:00
draft: false
title: Gentoo destroying earth?
type: post
url: /2008/10/10/gentoo-destroying-earth/
categories:
- Debian
- General
- Ubuntu
---

I worked a bit with some Gentoo systems the last days and it was no fun. The whole compiling thing is no fun. In fact, it is a danger for the environment. If every computer in the world run Gentoo, power consumption would increase dramatically. There would also be no netbooks, as they are almost unusable for running Gentoo on it, compiling software.

The path chosen by binary distributions like Debian is much better. Packages are compiled centrally and users download and install these pre-compiled packages. But it is also much less flexible in terms of which functionality is supported. We, as package maintainers, have to decide which functionality is likely to be used by the users. In Contrast, Gentoo has USE flags, which allows the user to enable the specific functionality he/she wants.

Should we combine the advantages of both technologies? Provide a normal binary distribution as we do now, but also provide a framework for users to easily recompile their packages, adding new functionality.

Imagine a combination of all these technologies:  User wants to install software X with feature F. The package maintainer has not enabled F in the binary. The user opens the website for his personal archive, selects the F flag and the software and clicks on build. The server builds the software and notifies the user once the binary is ready.

At Ubuntu, the first step has been made into this direction. While the package format is still the same, Launchpad allows users to create so-called PPAs (Personal Package Archives), where users can upload their source packages, which are then compiled and made available to other users. Let's say Project A releases version X of their software. They can create a source package for it, upload it to the PPA, and provide the binary packages to the users. Prior to PPAs, most users would have used an old version, compile their own version or use tarballs containing pre-compiled software (mozilla does this).

And sorry for the title. I respect the Gentoo community and the Gentoo developers, they are doing great work there. And ebuilds and Gentoo's boot system (with this runscript stuff) is really easy.

BTW: I also like the way Gentoo displays its boot messages. It looks much more organized than Debian's boot process. (In terms of the message logging, where Debian writes "done" when something is done, and Gentoo writes "[OK]" to the right side of the screen, in green letters. (This is partially possible in Debian using lsb-base-logging.sh, but not all init scripts use these functions, or they use the wrong ones.)
