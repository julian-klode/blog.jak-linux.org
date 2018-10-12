---
author: juliank
date: 2014-09-24 21:05:56+00:00
draft: false
title: 'APT 1.1~exp3 released to experimental: First step to sandboxed fetcher methods'
type: post
url: /2014/09/24/apt-1-1exp3-released-to-experimental-first-step-to-sandboxed-fetcher-methods/
---

Today, we worked, with the help of ioerror on IRC, on reducing the attack surface in our fetcher methods.

There are three things that we looked at:



	  1. Reducing privileges by setting a new user and group
	  2. chroot()
	  3. seccomp-bpf sandbox


Today, we implemented the first of them. Starting with 1.1~exp3, the APT directories /var/cache/apt/archives and /var/lib/apt/lists are owned by the "_apt" user (username suggested by pabs). The methods switch to that user shortly after the start. The only methods doing this right now are: copy, ftp, gpgv, gzip, http, https.

If privileges cannot be dropped, the methods will fail to start. No fetching will be possible at all.

Known issues:

  * We drop all groups except the primary gid of the user
  * copy breaks if that group has no read access to the files


We plan to also add chroot() and seccomp sandboxing later on; to reduce the attack surface on untrusted files and protocol parsing.

