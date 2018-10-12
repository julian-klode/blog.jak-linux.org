---
author: juliank
date: 2015-12-30 01:01:05+00:00
draft: false
title: APT 1.1.8 to 1.1.10 - going "faster"
type: post
url: /2015/12/30/apt-1-1-8-to-1-1-10-going-faster/
categories:
- Debian
- Ubuntu
---

Not only do I keep incrementing version numbers faster than ever before, APT also keeps getting faster. But not only that, it also has some bugs fixed and the cache is now checked with a hash when opening.



## Important fix for 1.1.6 regression


Since APT 1.1.6, APT uses the configured xz compression level. Unfortunately, the default was set to 9, which requires 674 MiB of RAM, compared to the 94 MiB required at level 6.

This caused the test suite to fail on the Ubuntu autopkgtest servers, but I thought it was just some temporary hickup on their part, and so did not look into it for the 1.1.7, 1.1.8, and 1.1.9 releases.  When the Ubuntu servers finally failed with 1.1.9 again (they only started building again on Monday it seems), I noticed something was wrong.

Enter git bisect. I created a script that compiles the APT source code and runs a test with ulimit for virtual and resident memory set to 512 (that worked in 1.1.5), and let it ran, and thus found out the reason mentioned above.

The solution: APT now defaults to level 6.


## New Features


APT 1.1.8 introduces `/usr/lib/apt/apt-helper cat-file` which can be used to read files compressed by any compressor understood by APT. It is used in the recent apt-file experimental release, and serves to prepare us for a future in which files on the disk might be compressed with a different compressor (such as LZ4 for Contents files, this will improve rred speed on them by factor 7).

David added a feature that enables servers to advertise that they do not want APT to download and use some Architecture: all contents when they include all in their list of architectures. This is to allow archives to drop Architecture: all packages from the architecture-specific content files, to avoid redundant data and (thus) improve the performance of apt-file.



## Buffered writes


APT 1.1.9 introduces buffered writing for rred, reducing the runtime by about 50% on a slowish SSD, and maybe more on HDDs. The 1.1.9 release is a bit buggy and might mess up things when a write syscall is interrupted, this is fixed in 1.1.10.


## Cache generation improvements


APT 1.1.9 and APT 1.1.10 improve the cache generation algorithms in several ways: Switching a lookup table from `std::map` to `std::unordered_map`, providing an inline `isspace_ascii()` function, and inlining the `tolower_ascii()` function which are tiny functions that are called a lot.

APT 1.1.10 also switches the cache's hash function to the DJB hash function and increases the default hash table sizes to the smallest prime larger than 15000, namely 15013. This reduces the average bucket size from 6.5 to 4.5. We might increase this further in the future.


## Checksum for the cache, but no more syncs


Prior to APT 1.1.10 writing the cache was a multi-part process:



	  1. Write the the cache to a temporary file with the dirty bit set to true
	  2. Call `fsync()` to sync the cache
	  3. Write a new header with the dirty bit set to false
	  4. Call `fsync()` to sync the new header
	  5. (Rename the temporary file to the target name)

The last step was obviously not needed, as we could easily live with an intact cache that has its dirty field set to false, as we can just rebuild it.

But what matters more is step 2. Synchronizing the entire 40 or 50 MB takes some time. On my HDD system, it consumed 56% of the entire cache generation time, and on my SSD system, it consumed 25% of the time.

APT 1.1.10 does not sync the cache at all. It now embeds a hashsum (adler32 for performance reasons) in the cache. This helps ensure that no matter what parts of the cache are written in case of some failure somewhere, we can still detect a failure with reasonable confidence (and even more errors than before).

This means that cache generation is now much faster for a lot of people. On the bad side, commands like apt-cache show that previously took maybe 10 ms to execute can now take about 80 ms.

Please report back on your performance experience with 1.1.10 release, I'm very interested to see if that works reasonably for other people. And if you have any other idea how to solve the issue, I'd be interested to hear them (all data needs to be written before the header with dirty=0 is written, but we don't want to sync the data).


## Future work


We seem to have a lot of temporary (?) `std::string` objects during the cache generation, accounting for about 10% of the run time. I'm thinking of introducing a `string_view` class similar to the one proposed for C++17 and make use of that.

I also thought about calling `posix_fadvise()` before starting to parse files, but the cache generation process does not seem to spend a lot of its time in system calls (even with all caches dropped before the run), so I don't think this will improve things.

If anyone has some other suggestions or patches for performance stuff, let me know.
