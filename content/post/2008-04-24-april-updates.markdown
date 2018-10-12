---
author: juliank
date: 2008-04-24 18:30:59+00:00
draft: false
title: April Updates
type: post
url: /2008/04/24/april-updates/
categories:
- Debian
- debimg
- General
- Ubuntu
---

This is a summary of most of my activities since end of march. BTW, I'm still at the T&S step in NM since January (I completed P&P in about 3 days). Also, thank you [Tolimar](http://blog.schmehl.info/) for being the second DD signing my key!


#### GNOME 2.22 (Python) / Updated Packages


At the end of march, I updated some GNOME packages. These packages were gnome-python and gnome-python-desktop. The upload of gnome-python-desktop was really important, because the old version depended on libtotem-plparser7, which was not available anymore, and FTBFS because the metacity API changed. This upload made other packages building and running again!

That time, I also uploaded new releases of dir2ogg and ndisgtk, which fixed some bugs.

On the first of April, I updated aufs to a new upstream snapshot, which fixed linux-modules-extra-2.6's FTBFS on armel, removed bashism in shell scripts, added a hack for limited splice support, and enabled building on -rt kernel (if the required functions are exported).


#### Packages To-Do


In the next week, I will upload a new aufs snapshot with support for kernel 2.6.25 and re-added support for kernels < 2.6.23. I will also update app-install-data to the current state of the archive.

Other stuff includes my ITA upload of gimmie and the upload of jockey, a tool to install drivers. Jockey will also be modified to provide the functionality from ndisgtk, which development has been discontinued as it is feature-complete (bug fixes will still be provided). Another package will be, of course, debimg 0.1 once it's released and of course the python-libisofs bindings.


#### Ubuntu packages


I requested syncs for dir2ogg and ndisgtk (after I uploaded sync'able versions to Debian) and for aria2, which was not installable before. I have also reported some bugs and used 8.04 for some time.


#### debimg stuff


I [released debimg 0.0.3](http://juliank.wordpress.com/2008/04/04/debimg-003-released/) on 4th April. This is the first release to require Python 2.5 and also the first release which uses the new media module, which provides a generic interface to disk creation.

I actually have not worked on debimg since that day, mainly because I did not have enough time. In May, I hope to add support for more architectures (at least theoretically, by providing a generic way of handling bootloaders and other non-packages and non-dists files) and release 0.1.

debimg 0.1 will not contain any features related to python-libisofs, because the focus is getting the basic functionality.

I have also not uploaded any new netinst build on jak-linux.org, since March.


##### debimg and the Debian Project News


Debimg will appear in the second issue of the Debian Project News, I'm currently working on the text for it. (BTW, I have also fixed one link in the first issue of the DPN)


##### debimg and Ubuntu


I [have suggested](https://lists.ubuntu.com/archives/ubuntu-devel-discuss/2008-April/003928.html) to switch Ubuntu's image building to debimg, and offered to do everything needed to do this. Given the speed of debimg and that the current features almost match the requirements of Ubuntu, this seems to be a great idea.


#### python-libisofs


As you may know, I released a first preview of the python-libisofs bindings some days ago, with almost complete support for creating image files. The next steps will be reading and growing images and of course, the bindings for libburn and libisoburn.


#### Switching from Ubuntu 8.04 to Debian unstable


I am currently working on migrating my laptop from Ubuntu 8.04 to Debian unstable, in order to be able to work better on my packages. Since most of my packages are sync'able now, this enables more efficient development. Another reason is to help the lenny release. This does not mean that I will be less active on the Ubuntu side, at least not much.

Let's make Debian Lenny and Ubuntu Intrepid the best releases ever.
