---
author: juliank
date: 2012-08-16 18:45:08+00:00
draft: false
title: Cleaning up the system with pseudo-boolean optimization
type: post
url: /2012/08/16/cleaning-up-the-system-with-pseudo-boolean-optimization/
categories:
- APT2
- Debian
- Python
---

You can use a PBO solver to clean up your system from unneeded automatically installed packages. First of all, you convert the system state to PB, and add an optimization function telling it to remove as many automatically installed packages as possible. Then you run this thing through a solver (such as clasp, which seems the fastest solver for PBO instances in the Debian archive) and convert its output to human-readable package names.

Code is provided at [http://anonscm.debian.org/gitweb/?p=users/jak/cleanup.git](http://anonscm.debian.org/gitweb/?p=users/jak/cleanup.git), under the MPL 2.0. You need to have python-apt and clasp installed to use it. There is potential minisat+ support, but it's currently a bit broken.

To use, run python program_builder.py, and it will tell you which packages are no longer needed on your system. It ignores Suggests, if you want those in, you have to hack the code and replace {"Recommends"} by {"Recommends", "Suggests"}. You can also turn of such dependencies by setting Program.hard_softdeps to False.
