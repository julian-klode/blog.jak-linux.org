---
author: juliank
date: 2009-05-14 19:50:39+00:00
draft: false
title: Ubuntu One
type: post
url: /2009/05/14/ubuntu-one/
categories:
- Ubuntu
---

Today, I was testing Canonical's new [Ubuntu One](http://ubuntuone.com/) service. Ubuntu One is a service for syncing and sharing files online, with 2GB storage for free. I installed the Ubuntu One client on Ubuntu 9.04 and it's cool.

Ubuntu One creates a directory named Ubuntu One in your home directory. Within this directory, there are two subdirectories. The first one is "My Files" and the second one is named "Shared With Me". When you place files in the "My Files" directory, the Ubuntu One client gets notified (using inotify) about the change and begins uploading the file to the Ubuntu one server.

When you access the web interface, which should work in every modern browser, and upload a file there, the next time your local client connects the files are fetched to your local hard disk. This also works when you have two different computers and create a file on the one computer, it will be visible on the second one as soon as it has fetched the new file.

You could also copy your .mozilla directory into the synced directory, and create a symlink from your home directory to it. I have not tried it myself, but in theory this would allow you to have your profile synced on all your computers.

And the best thing about Ubuntu One is that the client is completely free software and written in Python. This makes it possible to package the client for other distributions, like Debian. Packaging it for RPM-based distribution such as Fedora should also be doable, but may require some more time.

There seems to have been some criticism that the server side is not free software. While that may not be the good, it's certainly better than other services where even the client is proprietary. And there still is the possibility to write your own server as the protocol is available.

Ubuntu One is currently in private beta, if you want to try it out, you need an invitation (visit [ubuntuone.com](http://ubuntuone.com/) for further information).
