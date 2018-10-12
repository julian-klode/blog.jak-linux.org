---
author: juliank
date: 2008-02-14 22:12:30+00:00
draft: false
title: 'Ubuntu: aufs with casper 1.118 / ndisgtk 0.8.1 / ndisgtk in main?'
type: post
url: /2008/02/14/ubuntu-aufs-with-casper-1118-ndisgtk-081-ndisgtk-in-main/
categories:
- Ubuntu
---

Colin Watson today uploaded casper 1.118, now supporting aufs. To use aufs in future Ubuntu disks built with casper 1.118 or newer, use union=aufs. Please test it.

Another upload today was ndisgtk 0.8.1-1ubuntu1, bringing Ubuntu up-to-date with Debian and closing 3 bugs.

BTW, I requested to include ndisgtk in main, see [https://wiki.ubuntu.com/MainInclusionReportNdisgtk](https://wiki.ubuntu.com/MainInclusionReportNdisgtk). Having ndisgtk on the Ubuntu disks would be very useful for users without linux network drivers available and without enough experiences to use ndiswrapper from the commandline.
