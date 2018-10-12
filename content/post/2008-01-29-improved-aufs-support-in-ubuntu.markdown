---
author: juliank
date: 2008-01-29 22:23:00+00:00
draft: false
title: Improved aufs support in Ubuntu, Debian
type: post
url: /2008/01/29/improved-aufs-support-in-ubuntu/
categories:
- Debian
- Ubuntu
---

pre-compiled aufs modules for Ubuntu Hardy will be available soon. Today, the linux-ubuntu-modules git has seen the commit which adds the aufs module for generic and server kernels on the i386 and amd64 architectures.

But this is not the only thing. 5 patches from the aufs source have been [commited](http://kernel.ubuntu.com/git?p=ubuntu/ubuntu-hardy.git;a=commitdiff;h=3102668b1141ae9fd52ad869e48efa2128fa16d6) to Ubuntu Hardy's kernel repo.



	  1. [Export __lookup_hash](https://lists.ubuntu.com/archives/kernel-team/2008-January/002036.html): and is needed for NFS
	  2. [Export put_filp](https://lists.ubuntu.com/archives/kernel-team/2008-January/002037.html): This patch exports put_filp and is needed for NFS.
	  3. [Export do_splice_from and do_splice_to](https://lists.ubuntu.com/archives/kernel-team/2008-January/002038.html):
	  4. [Export security_inode_permission()](https://lists.ubuntu.com/archives/kernel-team/2008-January/002039.html), also used by UnionFS, where it is currently disabled
	  5. [Export deny_write_access()](https://lists.ubuntu.com/archives/kernel-team/2008-January/002040.html):

The aufs source package will see an update in Debian soon, which will be sync'ed into Ubuntu Hardy. This update uses the same code as the aufs code in linux-ubuntu-modules. This new code has improved XFS support, improved TMPFS support, improved support for lhash and put_filp patches. It's also the first revision to support kernel 2.6.24.

In the next days, we may see first disks using aufs. I'll provide patches for the software tomorrow. If nothing goes wrong, Ubuntu Hardy disks may use aufs instead of UnionFS, which may still be provided as a fallback.
