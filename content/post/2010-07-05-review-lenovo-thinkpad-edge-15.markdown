---
author: juliank
date: 2010-07-05 14:27:52+00:00
draft: false
title: 'Review: Lenovo ThinkPad Edge 15'
type: post
url: /2010/07/05/review-lenovo-thinkpad-edge-15/
categories:
- General
---

Wednesday, after some weeks with a flickering screen (or more precisely, something is causing GTK+ to redraw and the kernel to print ^@ in the terminal when you touch the screen, see [http://jak-linux.org/tmp/20100628_002.mp4](http://jak-linux.org/tmp/20100628_002.mp4)) in my 3 years old HP Compaq 6720s (which seems to be a software-hardware combination problem, at least it works in Ubuntu); I decided to buy a new laptop. It took me a few minutes to find the Lenovo ThinkPad Edge 15 NVL7VGE; which I ordered at [notebooksbilliger.de](http://www.notebooksbilliger.de/) at around 14:30 CEST using Express. On Thursday morning at 6:40 CEST, the device arrived.

[![](http://juliank.files.wordpress.com/2010/07/20100702_006.jpg?w=300)
](http://juliank.files.wordpress.com/2010/07/20100702_006.jpg)

The laptop features an Intel Core i5 430 M processor with integrated graphics, 4 GiB of RAM, 320 GB hard disk storage, matte screen, and of course a TrackPoint. The machine comes pre-installed with Windows 7 Professional which is not very nice (and Lenovo does not take Windows licenses back). I booted Ubuntu 10.04 from an USB disk which worked a few times, but not always, so I upgraded the BIOS to make USB booting reliable (as Lenovo published multiple BIOS updates already, one fixing this USB booting issue).

The first step was booting Ubuntu 10.04 from an USB hard disk to check the Linux support. Using Ubuntu, everything worked out of the box, including stuff like HDMI audio support or output switching. An exception may be the DVD drive, which only works if you set the SATA mode to compatibility. Non-DVD media also works in AHCI mode, but only if you start with a disc inserted in the drive. Playing DVDs requires setting a region code using setregion(8) [otherwise they do not work at all] and SATA compatibility mode [otherwise they only work partially].

Another issue is the HDMI output, as the TV is not correctly detected and some parts at the top and the bottom of the image are missing (that is, the GNOME panels) (but that happens with different screens and ATI cards as well). Oh, and closing the lid with a screen attached and the internal screen disabled works only as long as you do not open it again, because that causes the GPU to stop.

On the input side, we have one keyboard, one TrackPoint, and a touch pad. All of them work out of the box, but they have a few problems on the hardware side: The cursor keys on the keyboard are incredibly small and the touchpad is very large. The keyboard is different from the one in the HP Compaq: First of all, there is space between the keys (like Apple keyboards); and secondly, you need to apply more pressure in order to use the keys.

[![](http://juliank.files.wordpress.com/2010/07/20100702_007b.jpg?w=300)
](http://juliank.files.wordpress.com/2010/07/20100702_007b.jpg)

The device feels more solid than the HP Compaq 6720s, especially touching the screen does not change the colors on the screen. I don't know how long the keyboard will last, but I hope that I will still have symbols on them in 5 months (which was not the case for the HP Compaq 6720s keyboard).

Power consumption is another interesting point. When the device is idle and the screen is disabled, the device seems to consume about 10W. With screen enabled, consumption varies between 13W (idle) - 35W (building source code); if the values received via ACPI are correct. The device ships with a 48 Wh battery which after some time was displayed as 53 Wh in gnome-power-statistics (only the 'when loaded' state, capacity is displayed as 47.5Wh). According to Lenovo, the laptop lasts 4.5 hours on battery, meaning consumption of 47.5 Wh / 4.5 h = 10.5 Wh which is a bit overly optimistic if you want to work on the device.

After checking everything, I took over my Debian sid installation from my old laptop (which I installed in 2008). It runs happely now, although I still need to get accustomed to the new keyboard and the large touch pad.

All in all, the price of 765€ I paid for the device seems to be OK. Now I only need to remove the Windows 7 sticker and hope that the device lasts long enough until I want to buy a new one (probably 2013, if the aliens don't invade us 2012).
