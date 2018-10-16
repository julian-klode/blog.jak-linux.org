---
author: juliank
date: 2017-08-17 19:47:49+00:00
draft: false
title: Why TUF does not shine (for APT repositories)
type: post
url: /2017/08/17/why-tuf-does-not-shine-for-apt-repositories/
categories:
- Debian
- Ubuntu
---

In DebConf17 there was a talk about The Update Framework, short TUF. TUF claims to be a plug-in solution to software updates, but while it has the same practical level of security as apt, it also has the same shortcomings, including no way to effectively revoke keys.

TUF divides signing responsibilities into roles: A root role, a targets rule (signing stuff to download), a snapshots rule (signing meta data), and a time stamp rule (signing a time stamp file). There also is a mirror role for signing a list of mirrors, but we can ignore that for now. It strongly recommends that all keys except for timestamp and mirrors are kept offline, which is not applicable for APT repositories - Ubuntu updates the repository every 30 minutes, imagine doing that with offline keys. An insane proposal.

In APT repositories, we effectively only have a snapshots rule - the only thing we sign are Release files, and trust is then chained down by hashes (Release files hashes Packages index files, and they have hashes of individual packages). The keys used to sign repositories are online keys, after all, all the metadata files change every 30 minutes (Ubuntu) or 6 hours (Debian) - it's impossible to sign them by hand. The timestamp role is replaced by a field in the Release file specifying until when the Release file is considered valid.

Let's check the [attacks TUF protects again](https://github.com/theupdateframework/tuf/blob/develop/docs/tuf-spec.md#1-introduction):

  * Arbitrary installation attacks. - We protect against that with the outer signature and hashes
  * Endless data attacks. - Yes, we impose a limit on Release files (the sizes of other files are specified in there and this file is signed)
  * Extraneous dependencies attacks - That's verified by the signed hashes of Packages files
  * Fast-forward attacks - same
  * Indefinite freeze attacks - APT has a Valid-Until field that can be used to specify a maximum life time of a release file
  * Malicious mirrors preventing updates. - Well, the user configures the mirror, so usually not applicable. if the user has multiple mirrors, APT deals with that fine
  * Mix-and-match attacks - Again, signed Release file and hashes of other files
  * Rollback attacks - We do not allow Date fields in Release files to go backwards
  * Slow retrieval attacks - TUF cannot protect against that either. APT has very high timeouts, and there is no reasonable answer to that.
  * Vulnerability to key compromises - For our purposes where we need all repository signing keys to be online, as we need to sign new releases and metadata fairly often, it does not make it less vulnerable to require a threshold of keys (APT allows repositories to specify concrete key ids they may be signed with though, that has the same effect)
  * Wrong software installation. - Does not happen, the .deb files are hashed in the Packages files which are signed by the release file


As we can see, APT addresses all attacks TUF addresses.

But both do not handle key revocation. So, if a key & mirror gets compromised (or just key and the mirror is MITMed), we cannot inform the user that the key has been compromised and block updates from the compromised repository.

I just wrote up a [proposal to allow APT to query for revoked keys from a different host](https://lists.debian.org/deity/2017/08/msg00067.html) with a key revocation list (KRL) file that is signed by different keys than the repository. This would solve the problem of key revocation easily - even if the repository host is MITMed or compromised, we can still revoke the keys signing the repository from a different location.


