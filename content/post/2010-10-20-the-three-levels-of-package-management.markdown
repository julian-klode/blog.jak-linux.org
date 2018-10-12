---
author: juliank
date: 2010-10-20 15:01:47+00:00
draft: false
title: The Three Levels of Package Management
type: post
url: /2010/10/20/the-three-levels-of-package-management/
categories:
- APT2
- General
---

In today's Linux distributions, there are usually two to three levels of package management. In this blog post, I will explain the three levels of package management.


### 1. Local (dpkg, rpm)


The first level of package management is the 'local' level. This level consists of package management tools that install and/or remove packages via package archives such as .deb or .rpm files and a database of the local's system state.


### 2. Connected (APT, YUM, Smart)


The second level of package management is the 'connected' level. In this level, tools are fetching packages and information about them from (remote) locations known as 'repositories' or 'sources'. A level 2 package manager is usually built on top of a level 1 package manager, for example, APT uses dpkg - but there are also cases where one tool is both, such as opkg.


### 3. Abstract (PackageKit, Smart)


A level 3 package manager is a tool that supports different level 1 package managers via one generic interface. It may be implemented on top of a level 2 package manager (PackageKit), or may be implemented directly in level 2 (Smart).


### Conclusion: Merge Level 2 and 3


Most level 2 package managers share a great deal of tasks, such as solving dependency problems. Merging level 2 package management and level 3 package management would enable us to reduce the number of dependency problem solvers and combine our efforts into a few package managers. Such an implementation would need to be written in C and support all common level 1 package managers in order to be successful. As some might have guessed, this is what I plan to do with the project codenamed APT2, although work is not progressing very fast.


### PS: Back from vacation


I spent the more than the complete last week in (mostly rainy) Corfu, Greece and am now getting back to my usual development stuff. I have already processed my news & blogs backlog (1000+ messages) and will now start with my email backlog, so don't be angry if the answer to your email takes some time.
