---
author: juliank
date: 2016-10-25 16:19:50+00:00
draft: false
title: Introducing DNS66, a host blocker for Android
type: post
url: /2016/10/25/introducing-dns66-a-host-blocker-for-android/
categories:
- Android
tags:
- Android ads blocking dns vpn
---

![ic_launcher](https://juliank.files.wordpress.com/2016/10/ic_launcher.png)


I'm proud (yes, really) to announce **DNS66**, my host/ad blocker for Android 5.0 and newer. It's been around since last Thursday on F-Droid, but it never really got a formal announcement.

DNS66 creates a local VPN service on your Android device, and diverts all DNS traffic to it, possibly adding new DNS servers you can configure in its UI. It can use hosts files for blocking whole sets of hosts or you can just give it a domain name to block (or multiple hosts files/hosts). You can also whitelist individual hosts or entire files by adding them to the end of the list. When a host name is looked up, the query goes to the VPN which looks at the packet and responds with NXDOMAIN (non-existing domain) for hosts that are blocked.

You can find DNS66 here:

  * on GitHub: [https://github.com/julian-klode/dns66](https://github.com/julian-klode/dns66)
  * on F-Droid: [https://f-droid.org/app/org.jak_linux.dns66](https://f-droid.org/app/org.jak_linux.dns66)

F-Droid is the recommended source to install from. DNS66 is licensed under the GNU GPL 3, or (mostly) any later version.


## Implementation Notes


DNS66's core logic is based on another project, [dbrodie/AdBuster](https://github.com/dbrodie/AdBuster), which arguably has the cooler name. I translated that from Kotlin to Java, and cleaned up the implementation a bit:

All work is done in a single thread by using poll() to detect when to read/write stuff. Each DNS request is sent via a new UDP socket, and poll() polls over all UDP sockets, a Device Socket (for the VPN's tun device) and a pipe (so we can interrupt the poll at any time by closing the pipe).

We literally redirect your DNS servers. Meaning if your DNS server is 1.2.3.4, all traffic to 1.2.3.4 is routed to the VPN. The VPN only understands DNS traffic, though, so you might have trouble if your DNS server also happens to serve something else. I plan to change that at some point to emulate multiple DNS servers with fake IPs, but this was a first step to get it working with fallback: Android can now transparently fallback to other DNS servers without having to be aware that they are routed via the VPN.

We also need to deal with timing out queries that we received no answer for: DNS66 stores the query into a LinkedHashMap and overrides the removeEldestEntry() method to remove the eldest entry if it is older than 10 seconds or there are more than 1024 pending queries. This means that it only times out up to one request per new request, but it eventually cleans up fine.


