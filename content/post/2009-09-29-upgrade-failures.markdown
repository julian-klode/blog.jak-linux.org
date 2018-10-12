---
author: juliank
date: 2009-09-29 14:45:17+00:00
draft: false
title: upgrade failures
type: post
url: /2009/09/29/upgrade-failures/
categories:
- Debian
---

Today I wanted to upgrade my "sid" system again (like I do 1-3 times per day, especially when I have nothing else to do). First of all, I was hit by a bug in APT "Could not perform immediate configuration (2) on perl". I worked around it by running the latest git commit of cupt, which then started to upgrade my system. At some stage however, after upgrading parts of perl it seems, the progress stopped and perl complained that it could not find English.pm anymore. I tried to manually install the perl packages using dpkg -i, but this did not work. Then I just thought I should just try to unpack it and run dpkg -x <package> / on the perl packages. Now dpkg -i was working again and I could run dpkg -i on the packages again and continue my upgrade using apt-get.
