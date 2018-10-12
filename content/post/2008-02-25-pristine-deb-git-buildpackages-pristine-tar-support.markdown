---
author: juliank
date: 2008-02-25 20:48:41+00:00
draft: false
title: pristine-deb - git-buildpackage's pristine-tar support
type: post
url: /2008/02/25/pristine-deb-git-buildpackages-pristine-tar-support/
categories:
- Debian
- Ubuntu
---

Reading about the idea of pristine-deb, I actually noticed that using ar -rc file.deb debian-binary control.tar.gz data.tar.gz does not work, due to timestamps and other differences.

I am currently working on a pristine-deb program which will workaround all these issues. It will be able to work with git repositories like pristine-tar and uses pristine-tar for control.tar.gz and data.tar.gz. I may also add a function to decompress all compressed files (like changelog.gz) and uses pristine-gz to compress this file again before adding it to the tarball. This may save some additional space.

BTW, git-buildpackage now supports pristine-tar. Simply enable it with "pristine-tar = True"  in gbp.conf. Thank you Guido Guenther, for adding these patches.
