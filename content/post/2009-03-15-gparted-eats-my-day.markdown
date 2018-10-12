---
author: juliank
date: 2009-03-15 18:14:36+00:00
draft: false
title: GParted eats my day...
type: post
url: /2009/03/15/gparted-eats-my-day/
categories:
- General
---

Today, I wanted to shrink a partition by 5GB, and move it 5GB to the right. Well, I expected that it would take some minutes, but now it seems to take more than 5 hours, because GParted moves around the whole 87GB of the resized partition.

This is what happens:



	  * Check file system for errors (30min)
	  * Resize the file system (30min?)
	  * Resize the partition
	  * Check file system for errors (30min)
	  * Move the file system

	    * Read-only Simulation (!!!!!!!!!!!!!)
	    * Do it (~5 hours)



It really should tell me that it takes such a long time. I mean, why does it have to copy all 87GB, when all I want to do is get 5GB moved to the front? It should free these 5GB on the filesystem, move them to the end of the filesystem, decrease the partition size and finish.

It should not copy 87 GB 2 times, and should not run 2 filesystem checks without informing me before how long this will take. Now I wonder what happens when it resizes my 110 GB extended partition to 105 GB, and moves it?

Bad software, bad day.
