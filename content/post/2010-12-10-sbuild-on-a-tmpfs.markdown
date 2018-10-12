---
author: juliank
date: 2010-12-10 15:56:59+00:00
draft: false
title: sbuild on a tmpfs
type: post
url: /2010/12/10/sbuild-on-a-tmpfs/
categories:
- Debian
---

As some already know, is that I use sbuild to build all my packages in clean chroot environments. For this, I use the 'aufs' "mode" of schroot, that allows you to setup a chroot with one read-only base directory and one writeable overlay where changes are written to. 

One thing I had problems with was the time required to install build dependencies due to disk I/O. Given that I have 4G RAM in my computer, I decided to use a tmpfs as the writable overlay. For those of you who want to do the same, putting the following in /etc/fstab makes it work:




    
    
    overlay                     /var/lib/schroot/union/overlay tmpfs         defaults                    0       0
    







Build times are much faster this way because all write I/O is directed to the RAM
