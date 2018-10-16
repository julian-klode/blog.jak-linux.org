---
author: juliank
date: 2017-12-31 23:01:10+00:00
draft: false
title: A year ends, a new year begins
type: post
url: /2018/01/01/a-year-ends-a-new-year-begins/
categories:
- Debian
- General
- Ubuntu
---

2017 is ending. It's been a rather uneventful year, I'd say. About 6 months ago I started working on my master's thesis - it plays with adding linear types to Go - and I handed that in about 1.5 weeks ago. It's not really complete, though - you cannot actually use it on a complete Go program. The source code is of course [available on GitHub](https://github.com/julian-klode/lingolang), it's a bunch of Go code for the implementation and a bunch of Markdown and LaTex for the document. I'm happy about the code coverage, though: As a properly developed software project, it achieves about 96% code coverage - the missing parts happening at the end, when time ran out ;)

I released apt 1.5 this year, and started 1.6 with seccomp sandboxing for methods.

I went to DebConf17 in Montreal. I unfortunately did not make it to DebCamp, nor the first day, but I at least made the rest of the conference. There, I gave a talk about APT development in the past year, and had a few interesting discussions. One thing that directly resulted from such a discusssion was a new proposal for delta upgrades, with a very simple delta format based on a variant of bsdiff (with external compression, streamable patches, and constant memory use rather than linear). I hope we can implement this - the savings are enormous with practically no slowdown (there is no reconstruction phase, upgrades are streamed directly to the file system), which is especially relevant for people with slow or data capped connections.

This month, I've been buying a few "toys": I got a pair of speakers (JBL LSR 305), and I got a noise cancelling headphone (a Sony WH-1000XM2). Nice stuff. Been wearing the headphones most of today, and they're quite comfortable and really make things quite, except for their own noise ;) Well, both the headphone and the speakers have a white noise issue, but oh well, the prices were good.

This time of the year is not only a time to look back at the past year, but also to look forward to the year ahead. In one week, I'll be joining Canonical to work on Ubuntu foundation stuff. It's going to be interesting. I'll also be moving places shortly, having partially lived in student housing for 6 years (one room, and a shared kitchen), I'll be moving to a complete apartement.

On the APT front, I plan to introduce a few interesting changes. One of them involves automatic removal of unused packages: This should be happening automatically during install, upgrade, and whatever. Maybe not for all packages, though - we might have a list of "safe" autoremovals. I'd also be interested in adding metadata for transitions: Like if `libfoo1` replaces `libfoo0`, we can safely remove `libfoo0` if nothing depends on it anymore. Maybe not for all "garbage" either. It might make sense to restrict it to new garbage - that is packages that become unused as part of the operation. This is important for safe handling of existing setups with automatically removable packages: We don't suddenly want to remove them all when you run upgrade.

The other change is about sandboxing. You might have noticed that sometimes, sandboxing is disabled with a warning because the method would not be able access the source or the target. The goal is to open these files in the main program and send file descriptors to the methods via a socket. This way, we can avoid permission problems, and we can also make the sandbox stronger - for example, by not giving it access to the partial/ directory anymore.

Another change we need to work on is standardising the `Important` field, which is sort of like essential - it marks an installed package as extra-hard to remove (but unlike `Essential`, does not cause apt to install it automatically). The latest draft calls it `Protected`, but I don't think we have a consensus on that yet.

I also need to get happy eyeballs done - fast fallback from IPv6 to IPv4. I had a completely working solution some months ago, but it did not pass CI, so I decided to start from scratch with a cleaner design to figure out if I went wrong somewhere. Testing this is kind of hard, as it basically requires a broken IPv6 setup (well, unreachable IPv6 servers).

Oh well, 2018 has begun, so I'm going to stop now. Let's all do our best to make it awesome!
