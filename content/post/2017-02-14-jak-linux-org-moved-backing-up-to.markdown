---
author: juliank
date: 2017-02-14 23:51:38+00:00
draft: false
title: jak-linux.org moved / backing up
type: post
url: /2017/02/15/jak-linux-org-moved-backing-up-to/
categories:
- General
---

In the past two days, I moved my main web site jak-linux.org (and jak-software.de) from a very old contract at STRATO over to something else: The domains are registered with [INWX](https://www.inwx.de/) and the hosting is handled by [uberspace.de](https://uberspace.de/). Encryption is provided by [Let's Encrypt](https://letsencrypt.org/).

I requested the domain transfer from STRATO on Monday at 16:23, received the auth codes at 20:10 and the .de domain was transferred completely on 20:36 (about 20 minutes if you count my overhead). The .org domain I had to ACK, which I did at 20:46 and at 03:00 I received the notification that the transfer was successful (I think there was some registrar ACKing involved there). So the whole transfer took about 10 1/2 hours, or 7 hours since I retrieved the auth code. I think that's quite a good time :)

And, for those of you who don't know: uberspace is a shared hoster that basically just gives you an SSH shell account, directories for you to drop files in for the http server, and various tools to add subdomains, certificates, virtual users to the mailserver. You can also run your own custom build software and open ports in their firewall. That's quite cool.

I'm considering migrating the blog away from wordpress at some point in the future - having a more integrated experience is a bit nicer than having my web presence split over two sites. I'm unsure if I shouldn't add something like cloudflare there - I don't want to overload the servers (but I only serve static pages, so how much load is this really going to get?).



### in other news: off-site backups


I also recently started doing offsite backups via borg to a server operated by the wonderful [rsync.net](http://rsync.net/). For those of you who do not know rsync.net: You basically get SSH to a server where you can upload your backups via common tools like rsync, scp, or you can go crazy and use git-annex, borg, attic; or you could even just plain `zfs send` your stuff there.

The normal price is $0.08 per GB per month, but there is a [special borg price of $0.03](http://rsync.net/products/attic.html) (that price does not include snapshotting or support, really). You can also get a discounted normal account for $0.04 if you find the correct code on Hacker News, or other discounts for open source developers, students, etc. - you just have to send them an email.

Finally, I must say that uberspace and rsync.net feel similar in spirit. Both heavily emphasise the command line, and don't really have any fancy click stuff. I like that.
