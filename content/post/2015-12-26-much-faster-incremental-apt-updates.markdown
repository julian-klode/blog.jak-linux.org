---
author: juliank
date: 2015-12-26 19:01:37+00:00
draft: false
title: Much faster incremental apt updates
type: post
url: /2015/12/26/much-faster-incremental-apt-updates/
categories:
- Debian
tags:
- apt
- C
---

APT's performance in applying the Pdiffs files, which are the diff format used for Packages, Sources, and other files in the archive has been slow.


## Improving performance for uncompressed files


The reason for this is that our I/O is unbuffered, and we were reading one byte at a time in order to read lines. This changed on December 24, by adding read buffering for reading lines, vastly improving the performance of rred.

But it was still slow, so today I profiled - using gperftools - the rred method running on a 430MB uncompressed Contents file with a 75 KB large patch. I noticed that our ReadLine() method was calling some method which took a long time (google-pprof told me it was some _nss method, but that was wrong [thank you, addr2line]).

After some further look into the code, I noticed that we set the length of the buffer using the length of the line. And whenever we moved some data out of the buffer, we called `memmove()` to move the remaining data to the front of the buffer.

So, I tried to use a fixed buffer size of 4096 ([commit](http://anonscm.debian.org/cgit/apt/apt.git/commit/?id=0b29c72bdfc1466d47567cc3191b9661f81d3d3f)). Now `memmove() ` would spend less time moving memory around inside the buffer. This helped a lot, bringing the run time on my example file down from 46 seconds to about 2 seconds.

Later on, I rewrote the code to not use `memmove()` at all - opting for start and end variables instead; and increasing the start variable when reading from the buffer ([commit](http://anonscm.debian.org/cgit/apt/apt.git/commit/?id=83e22e26f9f10472aed97f889967c86ee218d28d)).

This in turn further improved things, bringing it down to about 1.6 seconds. We could now increase the buffer size again, without any negative effect.


### Effects on apt-get update


I measured the run-time of apt-get update, excluding appstream and apt-file files, for the update from todays 07:52 to the 13:52 dinstall run. Configured sources are unstable and experimental with amd64 and i386 architectures. appstream and apt-file indexes are disabled for testing, so only Packages and Sources indexes are fetched.

The results are impressive:



	  * For APT 1.1.6, updating with PDiffs enabled took 41 seconds.
	  * For APT 1.1.7, updating with PDiffs enabled took 4 seconds.

That's a tenfold increase in performance. By the way, running without PDiffs took 20 seconds, so there's no reason not to use them.


### Future work


Writes are still unbuffered, and account for about 75% to 80% of our runtime. That's an obvious area for improvements.

![rred-profile](https://juliank.files.wordpress.com/2015/12/rred-profile.png)



## Performance for patching compressed files


Contents files are usually compressed with gzip, and kept compressed locally because they are about 500 MB uncompressed and only 30MB compressed. I profiled this, and it turns out there is not much we can do about it: The majority of the time is spent inside zlib, mostly combining CRC checksums:

![rred-gz-profile](https://juliank.files.wordpress.com/2015/12/rred-gz-profile.png)


Going forward, I think a reasonable option might be to recompress Contents files using lzo - they will be a bit bigger (50MB instead of 30MB), but lzo is about 6 times as fast (compressing a 430MB Contents file took 1 second instead of 6).
