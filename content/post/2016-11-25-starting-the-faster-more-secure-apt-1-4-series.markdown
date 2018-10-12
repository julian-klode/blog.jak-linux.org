---
author: juliank
date: 2016-11-25 23:42:20+00:00
draft: false
title: Starting the faster, more secure APT 1.4 series
type: post
url: /2016/11/26/starting-the-faster-more-secure-apt-1-4-series/
categories:
- Debian
- Ubuntu
---

We just released the first beta of APT 1.4 to Debian unstable (beta here means that we don't know any other big stuff to add to it, but are still open to further extensions). This is the release series that will be released with Debian stretch, Ubuntu zesty, and possibly Ubuntu zesty+1 (if the Debian freeze takes a very long time, even zesty+2 is possible). It should reach the master archive in a few hours, and your mirrors shortly after that.


### Security changes


APT 1.4 by default disables support for repositories signed with SHA1 keys. I announced back in January that it was my intention to do this during the summer for development releases, but I only remembered the Jan 1st deadline for stable releases supporting that (APT 1.2 and 1.3), so better late than never.

Around January 1st, the same or a similar change will occur in the APT 1.2 and 1.3 series in Ubuntu 16.04 and 16.10 (subject to approval by Ubuntu's release team). This should mean that repository provides had about one year to fix their repositories, and more than 8 months since the release of 16.04. I believe that 8 months is a reasonable time frame to upgrade a repository signing key, and hope that providers who have not updated their repositories yet will do so as soon as possible.


### Performance work


APT 1.4 provides a 10-20% performance increase in cache generation (and according to callgrind, we went from approx 6.8 billion to 5.3 billion instructions for my laptop's configuration, a reduction of more than 21%). The major improvements are:

We switched the parsing of Deb822 files (such as Packages files) to my perfect hash function [TrieHash](https://github.com/julian-klode/triehash). TrieHash - which generates C code from a set of words - is about equal or twice as fast as the previously used hash function (and _two to three times faster_ than gperf), and we save an additional 50% of that time as we only have to hash once during parsing now, instead of during look up as well. APT 1.4 marks the first time TrieHash is used in any software. I hope that it will spread to dpkg and other software at a later point in time.vendors.

Another important change was to drop normalization of Description-MD5 values, the fields mapping a description in a Packages files to a translated description. We used to parse the hex digits into a native binary stream, and then compared it back to hex digits for comparisons, which cost us about 5% of the run time performance.

We also optimized one of our hash functions - the VersionHash that hashes the important fields of a package to recognize packages with the same version, but different content - to not normalize data to a temporary buffer anymore. This buffer has been the subject of some bugs (overflow, incompleteness) in the recent past, and also caused some slowdown due to the additional writes to the stack. Instead, we now pass the bytes we are interested in directly to our CRC code, one byte at a time.

There were also some other micro-optimisations: For example, the hash tables in the cache used to be ordered by standard compare (alphabetical followed by shortest). It is now ordered by size first, meaning we can avoid data comparisons for strings of different lengths. We also got rid of a std::string that cannot use short string optimisation in a hot path of the code. Finally, we also converted our case-insensitive djb hashes to not use a normal tolower_ascii(), but introduced tolower_ascii_unsafe() which just sets the "lowercase bit" (| 0x20) in the character.


### Others





	  * Sandboxing now removes some environment variables like TMP from the environment.
	  * Several improvements to installation ordering.
	  * Support for armored GPG keys in trusted.gpg.d.
	  * Various other fixes

For a more complete overview of all changes, consult the changelog.
