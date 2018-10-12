---
author: juliank
date: 2008-12-19 12:20:22+00:00
draft: false
title: 'Short review: Fedora 10 and Ubuntu 8.10'
type: post
url: /2008/12/19/short-review-fedora-10-and-ubuntu-810/
categories:
- General
- Ubuntu
---

After I tried OpenSolaris 2008.11, I also tried Fedora 10 and Ubuntu 8.10, each for almost one day.

**Creation of bootable USB stick:** For both distributions, I created a bootable USB stick because it is faster to install from USB than from CD/DVD. The creation was easy in both cases. Fedora ships a shell script and Ubuntu a graphical program for this task. Both very equally easy to use.

**Booting from USB: **Both distributions booted perfectly from USB. But there was a big difference in boot speed: Fedora 10 booted in about the same time Ubuntu needed to find the USB stick.

**Installation from USB to HDD:** Installation of both systems went very well, without any problems. Fedora's installer is far more powerful than Ubuntu's, e.g. it allows to use LVM or encrypted partitions. To setup LVM and encrypted volumes with Ubuntu, you need to use the text installer on Ubuntu's alternate disk (It's debian-installer). Ubuntu's graphical installer received a new partioning screen.

**Boot:** Fedora's boot time seems to have improved a lot since the last release. Ubuntu's boot time seems to be roughly the same as in 8.04. Both distributions provide a progress bar, whereas Ubuntu's usplash looks better. But this may change once kernel-based modesetting works on Intel cards in Fedora, because Fedora's splash program needs it for graphics. Else, it only displays ASCII progress bar.

**Login:** Fedora 10 shipped with GDM 2.24, which means that there are no themes yet. But this was no problem, as the non-themed design of GDM has improved a lot. I even like it more than any themed GDM I have seen. It reminds me a bit of OSX.

**Desktop:** Both distributions ship with GNOME 2.24. The default themes look good, whereas Fedora's uses more GNOME-like icons, whereas Ubuntu uses Human, which is based on Tango. And that is important for me, since I normally do not change any aspect of my desktop, except for adding cpu frequency and tomboy applets to the panel.

**Hardware support:** Both distributions provide good hardware support. Ubuntu leads here, at the cost of having non-free drivers included on the disk.For users needing windows wireless LAN drivers, Ubuntu is the right choice, as it ships ndiswrapper and the graphical frontend (ndisgtk) on the installation medium. Fedora does not include ndiswrapper, because of what it is used for (installing non-free Windows drivers). Both distributions **ship firmware, and consider firmware images as free enough, as they do not run on the CPU.**

**EXT4:** Fedora 10 ships with patches for EXT4 backported from Kernel 2.6.28. It also supports the installation on ext4 partitions, but only using the DVD and if booted with the ext4 option. The Live discs do not support installation to ext4.

**Package management:** Both distributions ship with good package managment software. YUM really improved since the early times, where it downloaded an extra metadata file for every package. Nowadays, yum and apt seem to be on a nearly equal level, but aptitude lets Ubuntu win, because it can handle problems much better  (ie. it proposes ways to solve problems) than YUM.

**Graphical package management:** Ubuntu wins here. Fedora only ships PackageKit for package managment, which, in my opinion, is not able to really compete with Synaptic and gnome-app-install.

**Conclusion:** Both distributions are very solid. Ubuntu still has the better package managment, and a bigger selection of packages. [This has only been possible due to Debian, which is the base of Ubuntu](http://www.ubuntu.com/community/ubuntustory/debian). I tried to write this blog post not as an Ubuntu member. I always liked Red Hat and Fedora, and one of my first Linux distributions was Red Hat 9.

**Links:**



	  * [http://www.heise-online.co.uk/open/What-s-new-in-Fedora-10--/features/112093](http://www.heise-online.co.uk/open/What-s-new-in-Fedora-10--/features/112093)
	  * [http://www.heise-online.co.uk/open/Ubuntu-8-10-first-tryout--/features/111823](http://www.heise-online.co.uk/open/Ubuntu-8-10-first-tryout--/features/111823)
	  * [http://fedoraproject.org/](http://fedoraproject.org/)
	  * [http://www.ubuntu.com/](http://www.ubuntu.com/)

