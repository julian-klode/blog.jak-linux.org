---
author: juliank
date: 2016-03-14 20:03:35+00:00
draft: false
title: Dropping SHA-1 support in APT
type: post
url: /2016/03/14/dropping-sha-1-support-in-apt/
categories:
- Debian
- Ubuntu
---

Tomorrow <del>is the anniversary of Caesar's assassination</del> APT will see a new release, turning of support for SHA-1 checksums in Debian unstable and in Ubuntu xenial, the upcoming LTS release.  While I have no knowledge of an imminent attack on our use of SHA1, Xenial (Ubuntu 16.04 LTS) will be supported for 5 years, and the landscape may change a lot in the next 5 years. As disabling the SHA1 support requires a bit of patching in our test suite, it's best to do that now rather than later when we're forced to do it.

This will mean that starting tomorrow, some third party repositories may stop working, such as the one for the web browser I am writing this with. Debian Derivatives should be mostly safe for that change, if they are registered in the Consensus, as that has checks for that. This is a bit unfortunate, but we have no real choice: Technical restrictions prevent us from just showing a warning in a sensible way.

There is one caveat, however: GPG signatures may still use SHA1. While I have prepared the needed code to reject SHA1-based signatures in APT, a lot of third party repositories still ship Release files signed with signatures using SHA-1 as the digest algorithms. Some repositories even still use 1024-bit DSA keys.

I plan to enforce SHA2 for GPG signatures some time after the release of xenial, and definitely for Ubuntu 16.10, so around June-August (possibly during DebConf). For xenial, I plan to have a SRU (stable release update) in January to do the same (it's just adding one member to an array). This should give 3rd party providers a reasonable time frame to migrate to a new digest algorithm for their GPG config and possibly a new repository key.

Summary



	  * Tomorrow: Disabling SHA1 support for Release, Packages, Sources files
	  * June/July/August: Disabling SHA1 support for GPG signatures (InRelease/Release.gpg) in development releases
	  * January 2017: Disabling SHA1 support for GPG signatures in Ubuntu 16.04 LTS via a stable-release-update.

