---
author: juliank
date: 2011-06-15 18:28:20+00:00
draft: false
title: dh-autoreconf v4 released, patching ltmain.sh for as-needed support
type: post
url: /2011/06/15/dh-autoreconf-v4-released-patching-ltmain-sh-for-as-needed-support/
categories:
- Debian
---

Yesterday I released version 4 of dh-autoreconf, fixing two bugs, and introducing a new feature: Patching ltmain.sh to make -Wl,--as-needed work.

For this new feature, run dh_autoreconf with the --as-needed option. dh_autoreconf will then patch all ltmain.sh equal to the system one (which should be all ltmain.sh files if libtoolize ran before or via dh_autoreconf). On clean, dh_autoreconf_clean reverses the patch again.

So, if your package runs autoreconf, and patches ltmain.sh via a patch you can now do this automatically via dh-autoreconf and be future-proof.

The only problem is that this might break once the patch no longer applies to libtool, at which point I need to update the package to include an updated patch. A solution for this problem would be to include the patch in libtool itself, as I proposed in [Bug#347650](http://bugs.debian.org/347650).

In case this works well, the option could also become the default which would make things even easier.
