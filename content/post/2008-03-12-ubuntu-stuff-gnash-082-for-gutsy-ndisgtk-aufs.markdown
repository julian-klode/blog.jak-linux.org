---
author: juliank
date: 2008-03-12 19:45:47+00:00
draft: false
title: 'Ubuntu stuff: gnash 0.8.2 for gutsy, ndisgtk, aufs'
type: post
url: /2008/03/12/ubuntu-stuff-gnash-082-for-gutsy-ndisgtk-aufs/
categories:
- Ubuntu
---

A backport of gnash 0.8.2 is available in my PPA at

    
    deb <a href="http://ppa.launchpad.net/juliank/ubuntu">http://ppa.launchpad.net/juliank/ubuntu</a> <span>gutsy</span> main


I wanted to try it, but I had no time to compile it, so I uploaded it to the PPA. The next day, I had a compiled backport.

I don't use it actively because it does not support some sites I visit.

Another news is the recent addition of ndisgtk to the ship and ship-live seeds, which means it will be available on the disk. [http://bazaar.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/ubuntu.hardy/revision/1223](http://bazaar.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/ubuntu.hardy/revision/1223).

BTW, recent Ubuntu Hardy images (including Alpha 6) have support for using aufs instead of unionfs,  simply add `union=aufs` to the kernel options. It may help if you have problems with unionfs and should be faster and more stable.
