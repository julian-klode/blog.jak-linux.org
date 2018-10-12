---
author: juliank
date: 2009-09-25 22:19:58+00:00
draft: false
title: 'APT2: config parser testing'
type: post
url: /2009/09/25/apt2-config-parser-testing/
categories:
- APT2
---

If you have an amd64 system, install the apt2 package from "deb http://people.debian.org/~jak/debian/ unstable/" and run the apt2-config command. Make sure that the parser reports no errors, otherwise send me an email or leave a comment here. One known exception is that all values must be quoted in the configuration file, I have no plans to fix this (probably just deprecate unquoted strings in APT instead). The parser is not as strict as cupt's parser, but it gives you more help if something wents wrong. We also ignore most semicolons for now (they will be turned into warnings or errors later on). It is using GScanner from GLib for parsing the files.

apt2-config replicates the functionality of apt-config. It currently do not read the configuration files in the correct order, so don't expect "apt2-config dump" to produce exactly the same output as "apt-config dump". To build APT2 yourself, you need a patch for waf from [http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=548329](http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=548329).
