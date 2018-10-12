---
author: juliank
date: 2008-04-20 17:07:52+00:00
draft: false
title: Fedora 9 & Kernel Mode Setting
type: post
url: /2008/04/20/fedora-9-preview/
categories:
- General
- Ubuntu
---

Today, I decided to try out the new kernel mode setting feature in Fedora 9, which moves some stuff about video from userspace into the kernel.

I tested this on my notebook, a HP Compaq 6720s with Intel X3100 (GM965) graphics controller.

I downloaded the preview live image for x86_64 and booted with the i915.modeset=1 option. The boot was almost normal, except that it was flicker-free. After the system booted I switched the virtual terminal from Xorg to tty1 and back, and it was extremely fast. The terminals all had the same resolution.

This does not mean that everything is perfect. There are a lot of things which do not work. For example, running glxgears and moving the window does not "look good". Also, speed was a bit low. Normally, in Ubuntu Hardy, I get about 1000 FPS, in Fedora I only got 230 FPS. But the difference was not visible.

Another thing which did not work was suspend & resume, because the graphics card seemed to be not correctly re-initialized. This is worse than Ubuntu & Debian. In Ubuntu, suspend & resume works almost every time. In Debian, it works except that the backlight is disabled in X.

If these problems can be fixed, it would be very interesting to get this feature into Ubuntu Intrepid, maybe not as the default, but as an option for people who want to test it.

Fedora 9 seems to be a fast and stable distribution, with experimental features for experienced users and developers. It also provides a nice application for configuring PulseAudio, like per-application volume settings, a functionality I miss in Ubuntu.
