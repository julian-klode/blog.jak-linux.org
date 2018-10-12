---
author: juliank
date: 2008-02-04 22:49:09+00:00
draft: false
title: Experiences with git and pristine-tar
type: post
url: /2008/02/04/experiences-with-git-and-pristine-tar/
categories:
- Debian
- General
- Ubuntu
---

In the last days, I used git very often. It was almost the first time I really used it, but I quickly understand the basic commands.

As some of you may know, the readahead-list package is now maintained in a [git repo](http://git.debian.org/?p=collab-maint/readahead-list.git;a=summary) in the collab-maint project. I decided to use git instead of bzr (which I used for everything before), because of its speed and because I wanted to learn more about git, how it works.

I used _git-import-dsc_ to import the first revision, and used _debdiffs_ from 1 to 2 and from 2 to 3 to import the next revisions. Afterwards, I run _git-import-orig_ on the new upstream tarball, which I downloaded and recompressed. Then, I did the packaging changes, added them using '_git add changed-file_' and committed them using _git commit_.

After I had done this, I read Planet Debian and saw Joey Hess's [post about the new features of pristine-tar 0.5](http://kitenet.net/~joey/blog/entry/generating_pristine_tarballs_from_git_repositories/), i.e. the integration with git. Running Ubuntu at the moment, I fetched the source package, built it and installed it.

I then opened a shell in my git repo and ran _pristine-tar commit path-to-orig upstream/0.20050517.0220_ to import the delta for the first tarball. Afterwards I did it for the second tarball.

Because I use git-buildpackage to build the package and Joey said he would like to see support for pristine-tar in git-buildpackage, I then wrote a patch for the programs in git-buildpackage to import and export the orig.tar.gz when needed.  The patch can be seen in [gitweb](http://git.debian.org/?p=users/jak-guest/git-buildpackage.git), and the maintainer responded in [Bug#463580](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=463580) will integrate the patch with some minor modifications.[
](//git.debian.org/git/users/jak-guest/git-buildpackage.gitgit://git.debian.org/git/users/jak-guest/git-buildpackage.git)

Both git and pristine-tar are great works, and it makes it so easy to maintain the readahead-list package. The combination of git, git-buildpackage and pristine-tar is the most powerful I ever used to maintain a Debian package, especially when you are not upstream.
