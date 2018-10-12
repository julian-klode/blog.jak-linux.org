---
author: juliank
date: 2016-09-02 19:43:25+00:00
draft: false
title: apt 1.3 RC4 - Tweaking apt update
type: post
url: /2016/09/02/tweaking-apt-update/
categories:
- Debian
- Ubuntu
---

Did that ever happen to you: You run apt update, it fetches a Release file, then starts fetching DEP-11 metadata, then any pdiff index stuff, and then applies them; all after another? Or this: You don't see any update progress until very near the end? Worry no more: I tweaked things a bit in 1.3~rc4 ([git commit](https://anonscm.debian.org/cgit/apt/apt.git/commit/?id=2a440328ea19e9646a93f847dd9eff21e03ad16d)).

Prior to 1.3~rc4, acquiring the files for an update worked like this: We create some object for the Release file, once a release file is done we queue any next object (DEP-11 icons, .diff/Index files, etc). There is no prioritizing, so usually we fetch the 5MB+ DEP-11 icons and components files first, and only then start working on other indices which might use Pdiff.

In 1.3~rc4 I changed the queues to be priority queues: Release files and .diff/Index files have the highest priority (once we have them all, we know how much to fetch). The second level of priority goes to the .pdiff files which are later on passed to the rred process to patch an existing Packages, Sources, or Contents file. The third priority level is taken by all other index targets.

Actually, I implemented the priority queues back in Jun. There was just one tiny problem: Pipelining. We might be inserting elements into our fetching queues in order of priority, but with pipelining enabled, stuff of lower priority might already have their HTTP request sent before we even get to queue the higher priority stuff.

Today I had an epiphany: We fill the pipeline up to a number of items (the depth, currently 10). So, let's just fill the pipeline with items that have the same (or higher) priority than the maximum priority of the already-queued ones; and pretend it is full when we only have lower priority items.

And that works fine: First the Release and .diff/Index stuff is fetched, which means we can start showing _accurate progress info_ from there one. Next, the pdiff files are fetched, meaning that we can _apply them in parallel_ to any targets downloading later in parallel (think DEP-11 icon tarballs).

This has a great effect on performance: For the 01 Sep 2016 03:35:23 UTC -> 02 Sep 2016 09:25:37 update of Debian unstable and testing with Contents and appstream for amd64 and i386, update time reduced from 37 seconds to 24-28 seconds.




## In other news


I recently cleaned up the apt packaging which renamed /usr/share/bug/apt/script to /usr/share/bug/apt. That broke on overlayfs, because dpkg could not rename the old apt directory to a backup name during unpack (only directories purely on the upper layer can be renamed). I reverted that now, so all future updates should be fine.

David re-added the Breaks against apt-utils I recently removed by accident during the cleanup, so no more errors about overriding dump solvers. He also added support for fingerprints in gpgv's GOODSIG output, which apparently might come at some point.

I Also fixed a few CMake issues, fixed the test suite for gpgv 2.1.15, allow building with a system-wide gtest library (we really ought to add back a pre-built one in Debian), and modified debian/rules to pass -O to make. I wish debhelper would do the latter automatically (there's a bug for that).

Finally, we fixed some uninitialized variables in the base256 code, out-of-bound reads in the Sources file parser, off-by-one errors in the tagfile comment stripping code[1], and some memcpy() with length 0. Most of these will be cherry-picked into the 1.2 (xenial) and 1.0.9.8 (jessie) branches (releases 1.2.15 and 1.0.9.8.4). If you forked off your version of apt at another point, you might want to do the same.

[1] those were actually causing the failures and segfaults in the unit tests on hurd-i386 buildds. I always thought it was a hurd-specific issue...

PS. Building for Fedora on OBS has a weird socket fd #3 that does not get closed during the test suite despite us setting CLOEXEC on it. Join us in #debian-apt on oftc if you have ideas.
