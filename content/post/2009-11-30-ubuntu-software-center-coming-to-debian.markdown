---
author: juliank
date: 2009-11-30 18:57:37+00:00
draft: false
title: Ubuntu Software Center coming to Debian
type: post
url: /2009/11/30/ubuntu-software-center-coming-to-debian/
categories:
- Debian
---

I just uploaded aptdaemon 0.11-1 and software-center 1.1debian1 to Debian unstable. They are currently waiting in NEW, and will hopefully pass it in a short time. I plan to replace gnome-app-install with software-center for Squeeze, but you can currently have both installed.

Ubuntu Software Center (or just 'Software Center') is a new graphical user interface for installing and removing applications; replacing gnome-app-install. Under the hood, it uses aptdaemon which exposes an interface to APT via D-Bus; i.e. something in the direction of PackageKit. At a later stage, the Software Center shall replace Synaptic, Update Manager and various other programs related to package management.

The aptdaemon package is completely compatible to the Ubuntu one, and could thus be synced directly to Ubuntu without any change (if Ubuntu supports "3.0 (quilt)" source packages now, I have not looked into this). The software-center package is based on the latest Ubuntu lucid package; and contains some generalization (e.g. replacing 'Ubuntu Software Center' with 'Software Center') at some more places. It still needs some work in the documentation and some parts of the program will have to be adjusted for Debian aswell. We also do not have a debianized icon yet; this will be worked on later.
