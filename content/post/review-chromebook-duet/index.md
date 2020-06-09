---
title: "Review: Chromebook Duet"
date: 2020-06-09T21:23:59+02:00
---

Sporting a beautiful 10.1" 1920x1200 display, the Lenovo IdeaPad Duet
Chromebook or Duet Chromebook, is one of the latest Chromebooks released,
and one of the few slate-style tablets, and it's only about 300 EUR (300 USD).
I've had one for about 2 weeks now, and here are my thoughts.

## Build & Accessories

The tablet is a fairly Pixel-style affair, in that the back has two components,
one softer blue one housing the camera and a metal feeling gray one. Build quality
is fairly good.

The volume and power buttons are located on the right side of the tablet, and
this is one of the main issues: You end up accidentally pressing the power button
when you want to turn your volume lower, despite the power button having a different
texture.

Alongside the tablet, you also find a kickstand with a textile back, and a
keyboard, both of which attach via magnets (and pogo pins for the keyboard).
The keyboard is crammed, with punctuation keys being halfed in size, and it
feels mushed compared to my usual experiences of ThinkPads and Model Ms, but
it's on par with other Chromebooks, which is surprising, given it's a tablet
attachment.

{{< figure src="/2020/06/09/review-chromebook-duet/chromebook-duet-assembled.jpg" caption="fully assembled chromebook duet" >}}

I mostly use the Duet as a tablet, and only attach the keyboard occasionally.
Typing with the keyboard on your lap is suboptimal.

My first Duet had a few bunches of dead pixels, so I returned it, as I had
a second one I could not cancel ordered as well. Oh dear. That one was fine!

## Hardware & Connectivity

The Chromebook Duet is powered by a Mediatek Helio P60T SoC, 4GB of RAM,
and a choice of 64 or 128 GB of main storage.

The tablet provides one USB-C port for charging, audio output (a 3.5mm adapter
is provided in the box), USB hub, and video output; though, sadly, the latter
is restricted to a maximum of 1080p30, or 1440x900 at 60 Hz. It can be charged
using the included 10W charger, or use up to I believe 18W from a higher powered
USB-C PD charger. I've successfully used the Chromebook with a USB-C monitor
with attached keyboard, mouse, and DAC without any issues.

On the wireless side, the tablet provides 2x2 Wifi AC and Bluetooth 4.2. WiFi
reception seemed just fine, though I have not done any speed testing, missing
a sensible connection at the moment. I used Bluetooth to connect to my smartphone
for instant tethering, and my Sony WH1000XM2 headphones, both of which worked
without any issues.

The screen is a bright 400 nit display with excellent viewing angles, 
and the speakers do a decent job, meaning you can use easily use this
for watching a movie when you're alone in a room and idling around. It has
a resolution of 1920x1200.

The device supports styluses following the USI standard. As of right now, the
only such stylus I know about is an HP one, and it costs about 70€ or so.

Cameras are provided on the front and the rear, but produce terrible images.

## Software: The tablet experience

The Chromebook Duet runs Chrome OS, and comes with access to Android apps
using the play store (and sideloading in dev mode) and access to full Linux
environments powered by LXD inside VMs.

The screen which has 1920x1200 is scaled to a ridiculous 1080x675 by default
which is good for being able to tap buttons and stuff, but provides next to no
content. Scaling it to 1350x844 makes things more balanced.

The Linux integration is buggy. Touches register in different places than where
they happened, and the screen is cut off in full screen extremetuxracer, making
it hard to recommend for such uses.

Android apps generally work fine. There are some issues with the back gesture
not registering, but otherwise I have not found issues I can remember.

One major drawback as a portable media consumption device is that Android apps
only work in Widevine level 3, and hence do not have access to HD content, and
the web apps of Netflix and co do not support downloading. Though one of the Duets
actually said L1 in check apps at some point (reported in [issue 1090330](https://bugs.chromium.org/p/chromium/issues/detail?id=1090330)).
It's also worth
noting that Amazon Prime Video only renders in HD, unless you change your
user agent to say you are Chrome on Windows - bad Amazon!

The tablet experience also lags in some other ways, as the palm rejection is
overly extreme, causing it to reject valid clicks close to the edge of the display
(reported in [issue 1090326](https://bugs.chromium.org/p/chromium/issues/detail?id=1090326)).

The on screen keyboard is terrible. It only does one language at a time, forcing
me to switch between German and English all the time, and does not behave as you'd
expect it when editing existing words - it does not know about them and thinks
you are starting a new one. It does provide a small keyboard that you can
move around, as well as a draw your letters keyboard, which could come in
handy for stylus users, I guess. In any case, it's miles away from gboard on
Android.

Stability is a mixed bag right now. As of Chrome OS 83, sites (well only Disney+
so far...) sometimes get killed with SIGILL or SIGTRAP, and the device rebooted
on its own once or twice. Android apps that use the DRM sometimes do not start,
and the Netflix Android app sometimes reports it cannot connect to the servers.

## Performance

Performance is decent to sluggish, with micro stuttering in a lot of places. The
Mediatek CPU is comparable to Intel Atoms, and with only 4GB of RAM, and an entire
Android container running, it's starting to show how weak it is.

I found that Google Docs worked perfectly fine, as did websites such as
Mastodon, Twitter, Facebook. Where the device really struggled was Reddit,
where closing or opening a post, or getting a reply box could take 5 seconds
or more. If you are looking for a Reddit browsing device, this is not for you.
Performance in Netflix was fine, and Disney+ was fairly slow but still usable.

All in all, it's acceptable, and given the price point and the build quality,
probably the compromise you'd expect.

## Summary

tl;dr:
* good: Build quality, bright screen, low price, included accessories
* bad: DRM issues, performance, limited USB-C video output, charging speed, on-screen keyboard, software bugs

The Chromebook Duet or IdeaPad Duet Chromebook is a decent tablet that is built
well above its price point. It's lackluster performance and DRM woes make it
hard to give a general recommendation, though. It's not a good laptop.

I can see this as the perfect note taking device for students, and as a 
cheap tablet for couch surfing, or as your on-the-go laptop replacement,
if you need it only occasionally.

I cannot see anyone using this as their main laptop, although I guess some
people only have phones these days, so: what do I know?

I can see you getting this device if you want to tinker with Linux on ARM, as
Chromebooks are quite nice to tinker with, and a tablet is super nice.
