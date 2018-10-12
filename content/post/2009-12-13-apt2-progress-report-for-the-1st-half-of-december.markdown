---
author: juliank
date: 2009-12-13 20:07:09+00:00
draft: false
title: APT2 progress report for the 1st half of December
type: post
url: /2009/12/13/apt2-progress-report-for-the-1st-half-of-december/
categories:
- APT2
---

This week was successful. I have pushed some changes from November to the repository which change the license to LGPL-2.1+ (which makes bi-directional sharing of code with other projects easier, since most Vala code is under the same license) and implement HTTP using libsoup2.4 directly, instead of using GIO and GVFS for this. I also added a parser for the sources.list format which uses regular expressions to parse the file and is relatively fast. The code needs a current checkout of Vala's git master to work correctly; as released versions had a bug which I noticed today and Jürg Billeter fixed in Vala 25 minutes later; thank you Jürg.

While nothing else happened in the public repository, the internal branch has seen a lot of new code; including SQLite 3 caches; Acquire text progress handling; and capt; the command-line advanced package tool. Most of the code will need to be reworked before it will be published, but I hope to have this completed until Christmas. It will also depend on Vala 0.7.9 or newer, which is yet to be released.

The decision to use SQLite 3 as a backend means that we won't see the size limitations APT has and that development can be simplified by using SQL queries for filtering requests. It also means that APT2 will be very fast in most actions, like searching; which currently happens in 0.140 seconds (unstable,experimental and more repositories enabled), whereas aptitude takes 1.101 seconds, cupt (which has no on-disk cache) 1.292 seconds, and apt-cache 0.475 seconds. Searching is performed by one SQL query. I also want to thank Jens Georg <mail@jensge.org>, who wrote Rygel's Database class which is also used with minor modifications (like defaulting to in-memory journals) in APT2 as well. Rygel.Database is a small wrapper around sqlite3 which makes it easier to program for Vala programmers.

The command-line application 'capt' provides a shell based on readline with history (and later on command completion) as well as direct usage like 'capt config dump' or 'capt search python-apt'. Just as with Eugene's cupt, 'capt' will be the only program in the core APT2 distribution and provide the same functionality currently provided by apt-get, apt-config and friends. The name is not perfect and can be easily confused with 'cupt', but it was the closest option for now; considering that the name 'apt' is already used by Java (for its "Annotation Processing Tool").

That's all for now, I'll tell you once all those features have passed my QA, and there is really something usable in the repository. In the meanwhile, you can discuss external dependency solvers, database layouts and other stuff in their threads on deity@lists.debian.org.

And a 'screenshot' from capt:

    
    
    jak@hp:~/Desktop/APT2:temp$ capt
    apt$ help
    APT2 0.0.20091213 command-line frontend
    
    Commands:
      config dump               Dump the configuration
      config get OPTION         Get the given option
      config set OPTION VALUE   Set the given option
      search EXPRESSION         Search for the given expression
      show PACKAGE              Show all versions of the given package
      sources list              Print a list of all sources
      version                   Print the version of APT2
    apt$ search python-apt
    build-depends-python-apt - Dummy package to fulfill package dependencies
    python-apt - Python interface to libapt-pkg
    python-apt-dbg - Python interface to libapt-pkg (debug extension)
    python-apt-dev - Python interface to libapt-pkg (development files)
    python-aptdaemon - Python module for the server and client of aptdaemon
    python-aptdaemon-gtk - Python GTK+ widgets to run an aptdaemon client
    apt$ 
    
