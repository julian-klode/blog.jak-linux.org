---
author: juliank
date: 2009-08-19 12:07:43+00:00
draft: false
title: notify-osd in Debian
type: post
url: /2009/08/19/notify-osd-in-debian/
categories:
- Debian
---

I forgot to write about this but I uploaded notify-osd to Debian some time ago which brings the passive notification bubbles known from Ubuntu. There are still some applications that do not behave correctly when using notify-osd. One example is giver which utilizes buttons on the notifications to accept or reject file transfers - As notify-osd is passive, it just displays a notification without the buttons. Using the notify plugin for Pidgin is also no good idea, as it now creates dialogs instead of displaying notifications, due to some (unneeded) buttons on the notification.

I personally don't like passive notifications that much, as I loose the control over the stuff on my display because I can't close the notification once I read it. But I like the design of notify-osd's notifications.

In other news python-apt 0.7.92 is now available in experimental, accepted by ftpmasters 3 hours after it entered NEW.
