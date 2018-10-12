---
author: juliank
date: 2016-09-06 22:12:12+00:00
draft: false
title: 'New software: sicherboot'
type: post
url: /2016/09/07/new-software-sicherboot/
categories:
- Debian
- sicherboot
tags:
- efi
- full disk encryption
- gummiboot
- luks
- secure boot
- systemd
- systemd-boot
- uefi
---

[![Fork me on GitHub](https://camo.githubusercontent.com/365986a132ccd6a44c23a9169022c0b5c890c387/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f7265645f6161303030302e706e67)
](https://github.com/julian-klode/sicherboot)

Today, I wrote _[sicherboot](https://github.com/julian-klode/sicherboot)_, a tool to integrate systemd-boot into a Linux distribution in an entirely new way: With secure boot support. To be precise: The use case here is to only run trusted code which then unmounts an otherwise fully encrypted disk, as in my setup:

![screenshot-from-2016-09-06-04-09-52](https://juliank.files.wordpress.com/2016/09/screenshot-from-2016-09-06-04-09-52.png)


If you want, sicherboot automatically creates db, KEK, and PK keys, and puts the public keys on your EFI System Partition (ESP) together with the KeyTool tool, so you can enroll the keys in UEFI. You can of course also use other keys, you just need to drop a db.crt and a db.key file into `/etc/sicherboot/keys`. It would be nice if sicherboot could enroll the keys directly in Linux, but there seems to be a [bug in efitools](https://bugs.debian.org/836770) preventing that at the moment. For some background: The Platform Key (PK) signs the Key Exchange Key (KEK) which signs the database key (db). The db key is the one signing binaries.

sicherboot also handles installing new kernels to your ESP. For this, it combines the kernel with its initramfs into one executable UEFI image, and then signs that. Combined with a fully encrypted disk setup, this assures that only you can run UEFI binaries on the system, and attackers cannot boot any other operating system or modify parts of your operating system (except for, well, any block of your encrypted data, as XTS does not authenticate the data; but then you do have to know which blocks are which which is somewhat hard).

sicherboot integrates with various parts of Debian: It can work together by dracut via an evil hack (diverting dracut's `kernel/postinst.d` config file, so we can run sicherboot after running dracut), it should support initramfs-tools (untested), and it also integrates with systemd upgrades via triggers on the `/usr/lib/systemd/boot/efi` directory.

Currently sicherboot only supports Debian-style setups with `/boot/vmlinuz-<version>` and `/boot/initrd.img-<version`> files, it cannot automatically create combined boot images from or install boot loader entries for other naming schemes yet. Fixing that should be trivial though, with a configuration setting and some eval magic (or string substitution).

Future planned features include: (1) support for multiple ESP partitions, so you can have a fallback partition on a different drive (think RAID type situation, keep one ESP on each drive, so you can remove a failing one); and (2) a tool to create a self-contained rescue disk image from a directory (which will act as initramfs) and a kernel (falling back to a `vmlinuz` file )

It might also be interesting to add support for other bootloaders and setups, so you could automatically sign a grub cryptodisk image for example. Not sure how much sense that makes.

I published the source at [https://github.com/julian-klode/sicherboot](https://github.com/julian-klode/sicherboot) (MIT licensed) and uploaded the package to Debian, it should enter the NEW queue soon (or be in NEW by the time you read this). Give it a try, and let me know what you think.
