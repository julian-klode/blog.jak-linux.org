---
author: juliank
date: 2008-12-19 15:09:22+00:00
draft: false
title: Filesystems
type: post
url: /2008/12/19/filesystems/
categories:
- General
---

In the last months, I noticed that it was a bad decision to use XFS as my filesystem; and before I realized that ext3 was a bad choice as well.

File systems have problems. I can't use ext3 on my laptop, because it would check the whole disk (120GB) every 30 boots. And this check takes a very long time (15 or 30 minutes, I do not know it exactly). XFS is better, but also problematic because deleting a big directory with a deep hierarchy takes a very long time like 1.5 minutes , whereas ext3 needs a few seconds. Also I still wonder why XFS needs no checks.

Therefore I might go with ext4. The time needed to check the partition seemed to be much shorter and the speed is about the same as with ext3. The installation will probably be: Install Lenny on a ext3 partition, install kernel with ext4 support (which is kernel 2.6.28), add ext4 to /etc/initramfs-tools/modules, tar the partition, format it as ext4, and untar the contents again; because converting does not bring the advantags of ext4 to already existing files.

BTW, I did some benchmarking with bonnie++, and XFS had about 20,000 operations per second, whereas ext3 had 60,000. ext4dev from Kernel 2.6.27 was a bit slower than ext3

I also tested BTRFS, but BTRFS is 1) not stable enough 2) as slow as XFS. It also shows horrible write performance of 19MB/s using dd, whereas XFS reached 42MB/s. BTW, benchmarking btrfs with bonnie++ only works using "-s 0", i.e. without I/O performance test, else you receive a kernel bug. I subscribed to the btrfs mailing list, and sent my bug report email 4 times, but it never reached the list it seems. This bug also happens [in other cases](http://permalink.gmane.org/gmane.comp.file-systems.btrfs/1744).
