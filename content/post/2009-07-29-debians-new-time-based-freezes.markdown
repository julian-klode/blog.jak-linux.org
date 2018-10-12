---
author: juliank
date: 2009-07-29 12:34:29+00:00
draft: false
title: Debian's new time-based freezes
type: post
url: /2009/07/29/debians-new-time-based-freezes/
categories:
- Debian
- Ubuntu
---

Overall, having time-based freezes is a good idea. But the chosen cycle is problematic, especially if one considers Ubuntu's LTS release cycles. The problem is that if Debian releases a new version at approximately the same time as Ubuntu, there will not be much synchronization and Ubuntu will have newer program versions.

Consider the releases of Ubuntu 8.04 LTS (April 2008) and Debian GNU/Linux 5.0 (February 2009). Whereas Ubuntu 8.04 provides GNOME 2.22 including a new Nautilus, Debian provides GNOME 2.22 with nautilus 2.20. Ubuntu's release made at about the same time (Ubuntu 9.04) already included GNOME 2.26.

The reason for this are the different development processes. Whereas a Debian release is based on stable upstream versions, the development of Ubuntu releases happens using newest pre-releases, causing Ubuntu releases to be one generation ahead in most technologies, although released at the same time.

Another difference is the way of freezing and the duration of the total freeze. Ubuntu has a freeze process split into multiple stages. The freeze which is comparable to Debian's freeze is the feature freeze, which usually happens two months before the release. Debian's freeze happens 6 month before the release, just about the time when Ubuntu has just defined the features to be included in the next release.

Synchronizing the release cycles of Debian and Ubuntu basically means that Ubuntu will always provide the newer features, better hardware support, etc. Ubuntu is the winner of this decision. It will have less bugs because it inherits from a frozen Debian branch and it can include newer versions where required because it freezes 3 months later.

To synchronize the package versions shipped in Debian and Ubuntu you have to make your release schedules asynchronous, in a way that the Debian release freezes after the Ubuntu release. This basically means that I expect Debian 6.0 (2010/H1) to be more similar to Ubuntu 9.10 than to Ubuntu 10.04. I would have preferred to freeze Squeeze in December 2010 and release in April 2011, and Ubuntu LTS to be re-scheduled for October 2010.

Now let's say you are a Debian and Ubuntu user (and you prefer none of them) and you want to setup a new system in 2010/H2 (so the systems have a half year to stabilize). This system should be supported for a long time. You have two options: Debian 6.0 and Ubuntu 10.04. Which will you choose? Most people would probably consider Ubuntu now, because it provides better support for their hardware and has the newer features. A (partial) solution to this problem would be to make backports an official part of Debian starting with Debian 6.0.

Furthermore, there is the question of security support. If we want to provide the ability to upgrade directly from Debian 5.0 to Debian 7.0, we will have to support Lenny until 2012/H2 (to give users enough time to upgrade, when we release 7.0 in 2012/H1). This means that we would have to support in 2012: Debian 5.0, 6.0 and 7.0. And another side effect is that Debian 6.0 would have a 3 year security support, just like Ubuntu 10.04.

All in all, the decision means that Debian and Ubuntu LTS releases will occur at about the same time, will be supported for about the same time and that Ubuntu has the newer packages and less bugs to fix.
