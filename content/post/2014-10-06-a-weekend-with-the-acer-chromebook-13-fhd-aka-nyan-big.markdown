---
author: juliank
date: 2014-10-06 16:19:03+00:00
draft: false
title: A weekend with the Acer Chromebook 13 FHD (AKA nyan-big)
type: post
url: /2014/10/06/a-weekend-with-the-acer-chromebook-13-fhd-aka-nyan-big/
categories:
- Chromebook
tags:
- Linux
---

I spent the weekend using almost exclusively my Chromebook 13, on a single charge Saturday and Sunday.



### Keyboard


I think I like the keyboard better now than I used to when I first tried it. It gets nowhere near the ThinkPad X230 one, though; appart from the coating, which my (backlit) X230 unfortunately does not have.



### Screen


While the screen appeared very grainy to me on first sight, having only used IPS screens in the past year, I got used to it over the weekend. I now do not notice much graininess anymore. The contrast still seems extremely poor, the colors are not vivid, and the vertical viewing angles are still a disaster, though.



### Battery life


I think the battery life is awesome. I have 30% remaining now while I am writing this blog post and Chrome OS tells me I still have 3 hours and 19 minutes remaining. It could probably still be improved though, I notice that Chrome OS uses 7-14% CPU in idle normally (and up to 20% in exceptional cases).

The maximum power usage I measured using the battery's internal sensor was about 9.2W, that was with 5 Big Buck Bunny 1080p videos played in parallel. Average power consumption is around 3-5W (up to 6.5 with single video playing), depending on brightness, and use.



### Performance


While I do notice a performance difference to my much more high-end Ivy Bridge Core i5 laptop, it turns out to be usable enough to not make me want to throw it at a wall. Things take a bit longer than I am used to, but it is still acceptable.



### Input: Software Part



The user interface is great. There are a lot of gestures available for navigating between windows, tabs, and in the history. For example, horizontally swiping with two finger moves in history, three fingers moves between tabs; and swiping down (or up for Australian scrolling) gives an overview of all windows (like expose on Mac, GNOME's activities, or the multi-tasking thing Maemo used to have).

What I miss is a keyboard shortcut like Meta + Left/Right on GNOME which moves the active window to the left/right side of the screen. That would be very useful for mult-tasking situations.



### Issues



I noticed some performance issues. For example, I can easily get the Chromebook to use 85% of a CPU by scrolling on a page with the touchpad or 70% for scrolling by keeping a key pressed ([crbug.com/420452](http://crbug.com/420452)).

While watching Big Buck Bunny on YouTube, I noticed some (micro) stuttering in the beginning of the film, as well as each time I move in or out of the video area when not in full-screen mode ([crbug.com/420582](http://crbug.com/420582)). It also increases CPU usage to about 70%.



### Running a "proper" Linux?



Today, I tried to play around a bit with Debian wheezy and Ubuntu trusty systems, in a chroot for now. I was trying to find out if I can get an accelerated X server with the standard ChromeOS kernel. The short answer is: No. I tried two things:



	  1. Debian wheezy with the binaries from ChromeOS (they have the same xserver version)
	  2. Ubuntu trusty with the Nvidia drivers

Unfortunately, they did not work. Option 1 failed because ChromeOS uses glibc 2.15 whereas wheezy uses 1.13. Option 2 failed because the sysfs interface is different between the ChromeOS and Linux4Tegra kernels.

I guess I'll have to wait.

I also tried booting a custom kernel from USB, but given that the u-boot always sets console= and there is no non-verified u-boot available yet, I could not see any output on the screen :(  - Maybe I should build a u-boot myself?
