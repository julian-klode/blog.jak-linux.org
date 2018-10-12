---
author: juliank
date: 2009-01-11 20:02:25+00:00
draft: false
title: What have you done this week?
type: post
url: /2009/01/11/what-have-you-done-this-week/
categories:
- Debian
---

Well,

I wrote** 2599 lines** of documentation. More detailed I wrote 2599 lines of documentation from Thursday to Sunday.

In total, the jak branch of python-apt now has a diffstat (compared to debian-sid) of:

**Changes:** **113 files** changed, **5845 insertions** (+), **2763 deletions**(-)

Partly responsible is Ben Finney, whose patches I merged. I also closed 7 bugs not relevant anymore in current versions of python-apt.

This is the changelog to from debian-sid to jak:

    
    
    python-apt (0.7.9~exp2) experimental; urgency=low
    
      * apt/*.py:
        - Almost complete cleanup of the code
        - Remove inconsistent use of tabs and spaces (Closes: #505443)
        - Improved documentation
      * apt/debfile.py:
        - Drop get*() methods, as they are deprecated and were
          never in a stable release
        - Make DscSrcPackage working
      * apt/gtk/widgets.py:
        - Fix the code and document the signals
      * Introduce new documentation build with Sphinx
        - Contains style Guide (Closes: #481562)
        - debian/rules: Build the documentation here
        - setup.py: Remove pydoc building and add new docs.
        - debian/examples: Include examples from documentation
        - debian/python-apt.docs:
          + Change html/ to build/doc/html.
          + Add build/doc/text for the text-only documentation
      * setup.py:
        - Only create build/data when building, not all the time
        - Remove build/mo and build/data on clean -a
      * debian/control:
        - Remove the Conflicts on python2.3-apt, python2.4-apt, as
          they are only needed for oldstable (sarge)
        - Build-Depend on python-sphinx (>= 0.5)
      * aptsources/distinfo.py:
        - Allow @ in mirror urls (Closes: #478171) (LP: #223097)
      * Merge Ben Finney's whitespace changes (Closes: #481563)
      * Merge Ben Finney's do not use has_key() (Closes: #481878 )
      * Do not use deprecated form of raise statement (Closes: #494259)
      * Add support for PkgRecords.SHA256Hash (Closes: #456113)
    
     -- Julian Andres Klode   Sun, 11 Jan 2009 20:01:59 +0100
    



...

This will again close 7 bugs. But the most important part is to actually have the complete documentation (OK, some descriptions are missing, but all classes,functions,methods,attributes,data should be there now).

I still need to rearrange parts of the documentation and add some descriptions to some pieces, but all in all I am satisfied with what I have done this week.

Take a look at the documentation: [http://people.debian.org/~jak/python-apt-doc/apt/](http://people.debian.org/~jak/python-apt-doc/apt/), it received documentation for 9 new classes today.

I also added an entry to the DeveloperNews page on wiki.debian.org.
