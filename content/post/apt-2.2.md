---
title: "APT 2.2 released"
date: 2021-02-18T21:09:27+01:00
---

APT 2.2.0 marks the freeze of the 2.1 development series and the start of the 2.2 stable series.

Let's have a look at what changed compared to 2.2. Many of you who run Debian testing or unstable,
or Ubuntu groovy or hirsute will already have seen most of those changes.

## New features

* Various patterns related to dependencies, such as ?depends are now available (2.1.16)
* The `Protected` field is now supported.
  It replaces the previous `Important` field and is like Essential,
  but only for installed packages
  (some minor more differences maybe in terms of ordering the installs).
* The `update` command has gained an `--error-on=any` option that makes it error out on any failure,
  not just what it considers persistent ons.
* The `rred` method can now be used as a standalone program to merge pdiff files
* APT now implements [phased updates](https://wiki.ubuntu.com/PhasedUpdates).
  Phasing is used in Ubuntu to slow down and control the roll out of updates in the -updates pocket,
  but has previously only been available to desktop users using update-manager.

## Other behavioral changes

* The kernel autoremoval helper code has been rewritten from shell in C++ and now runs at run-time,
  rather than at kernel install time,
  in order to correctly protect the kernel that is running now,
  rather than the kernel that was running when we were installing the newest one.

  It also now protects only up to 3 kernels, instead of up to 4, as was originally intended,
  and was the case before 1.1 series.
  This avoids /boot partitions from running out of space, especially on Ubuntu which has boot
  partitions sized for the original spec.

## Performance improvements

* The cache is now hashed using XXH3 instead of Adler32 (or CRC32c on SSE4.2 platforms)
* The hash table size has been increased

## Bug fixes

* `*` wildcards work normally again (since 2.1.0)
* The cache file now includes all translation files in /var/lib/apt/lists,
  so multi-user systems with different locales correctly show translated descriptions now.
* URLs are no longer dequoted on redirects only to be requoted again,
  fixing some redirects where servers did not expect different quoting.
* Immediate configuration is now best-effort, and failure is no longer fatal.
* various changes to solver marking leading to different/better results in some cases (since 2.1.0)
* The lower level I/O bits of the HTTP method have been rewritten to hopefully improve stability
* The HTTP method no longer infinitely retries downloads on some connection errors
* The pkgnames command no longer accidentally includes source packages
* Various fixes from fuzzing efforts by David

## Security fixes

* Out-of-bound reads in ar and tar implementations (CVE-2020-3810, 2.1.2)
* Integer overflows in ar and tar (CVE-2020-27350, 2.1.13)

(all of which have been backported to all stable series,
 back all the way to 1.0.9.8.\* series in jessie eLTS)

## Incompatibilities

* N/A - there were no breaking changes in apt 2.2 that we are aware of.

## Deprecations

* `apt-key(1)` is scheduled to be removed for Q2/2022, and several new warnings have been added.

  apt-key was made obsolete in version 0.7.25.1, released in January 2010, by
  `/etc/apt/trusted.gpg.d` becoming a supported place to drop additional keyring files,
  and was since then only intended for deleting keys in the legacy `trusted.gpg` keyring.

  Please manage files in `trusted.gpg.d` yourself;
  or place them in a different location such as
  `/etc/apt/keyrings` (or make up your own, there's no standard location)
  or `/usr/share/keyrings`,
  and use signed-by in the sources.list.d files.

  The legacy `trusted.gpg` keyring still works, but will also stop working eventually.
  Please make sure you have all your keys in `trusted.gpg.d`.
  Warnings might be added in the upcoming months when a signature could not be verified using just trusted.gpg.d.

  Future versions of APT might [switch away from GPG](https://wiki.debian.org/Teams/Apt/Spec/AptSign).

* As a reminder, regular expressions and wildcards other than `*` inside package names are deprecated (since 2.0).
  They are not available anymore in apt(8), and will be removed for safety reasons in apt-get in a later release.
