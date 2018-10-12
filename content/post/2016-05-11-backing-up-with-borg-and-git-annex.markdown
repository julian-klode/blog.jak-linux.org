---
author: juliank
date: 2016-05-11 09:47:42+00:00
draft: false
title: Backing up with borg and git-annex
type: post
url: /2016/05/11/backing-up-with-borg-and-git-annex/
---

I recently found out that I have access to a 1 TB cloud storage drive by 1&1, so I decided to start taking off-site backups of my $HOME (well, backups at all, previously I only mirrored the latest version from my SSD to an HDD).

I initially tried obnam. Obnam seems like a good tool, but is insanely slow. Unencrypted it can write about 3 MB/s, which is somewhat OK, but even then it can spend hours forgetting generations (1 generation takes probably 2 minutes, and there might be 22 of them). In encrypted mode, the speed reduces a lot, to about 500 KB/s if I recall correctly, which is just unusable.

I found borg backup, a fork of attic. Borg backup achieves speeds of up to 15 MB/s which is really nice. It's also faster with scanning: I can now run my bihourly backups in about 1 min 30s (usually backs up about 30 to 80 MB - mostly thanks to Chrome I suppose!). And all those speeds are with encryption turned on.

Both borg and obnam use some form of chunks from which they compose files. Obnam stores each chunk in its own file, borg stores multiple chunks (even from different files) in a single pack file which is probably the main reason it is faster.

So how am I backing up: My laptop has an internal SSD and an HDD.  I backup every 2 hours (at 09,11,13,15,17,19,21,23,01:00 hours) using a systemd timer event, from the SSD to the HDD. The backup includes all of $HOME except for Downloads, .cache, the trash, Android SDK, and the eclipse and IntelliJ IDEA IDEs.

Now the magic comes in: The backup repository on the HDD is monitored by git-annex assistant, which automatically encrypts and uploads any new files in there to my 1&1 WebDAV drive and registers them in a git repository hosted on bitbucket. All files are encrypted and checksummed using SHA256, reducing the chance of the backup being corrupted.

I'm not sure how the WebDAV thing will work once I want to prune things, I suspect it will then delete some pack files and repack things into new files which means it will spend more bandwidth than obnam would. I'd also have to convince git-annex to actually drop anything from the WebDAV remote, but that is not really that much of a concern with 1TB storage space in the next 2 years at least...

I also have an external encrypted HDD which I can take backups on, it currently houses a fuller backup of $HOME that also includes Downloads, the Android SDK, and the IDEs for quicker recovery. Downloads changes a lot, and all of them can be fairly easily re-retrieved from the internet as needed, so there's not much point in painfully uploading them to a WebDAV backup site.


