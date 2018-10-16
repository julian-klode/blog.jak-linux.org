---
author: juliank
date: 2016-03-15 19:25:00+00:00
draft: false
title: Clarifications and updates on APT + SHA1
type: post
url: /2016/03/15/clarifications-and-updates-on-apt-sha1/
categories:
- Debian
- Ubuntu
---

The APT 1.2.7 release is out now.

Despite of what I wrote earlier, we now print warnings for Release files signed with signatures using SHA1 as the digest algorithm. This involved extending the protocol APT uses to communicate with the methods a bit, by adding a new 104 Warning message type.

    W: gpgv:/var/lib/apt/lists/apt.example.com_debian_dists_sid_InRelease: The repository is insufficiently signed by key
    1234567890ABCDEF0123456789ABCDEF01234567 (weak digest)
    


Also note that SHA1 support is not dropped, we merely do not consider it trustworthy. This means that it feels like SHA1 support is dropped, because sources without SHA2 won't work; but the SHA1 signatures will still be used in addition to the SHA2 ones, so there's no point removing them (same for MD5Sum fields).

We also fixed some small bugs!
