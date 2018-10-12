---
author: juliank
date: 2009-02-01 22:32:15+00:00
draft: false
title: Really, don't use codenames for pinning.
type: post
url: /2009/02/02/really-dont-use-codenames-for-pinning/
categories:
- Debian
---

You can not use codenames for pinning packages to a specific release. Everything like this just fails, and can result in apt not finding any candidate for a package. You can see this for example in Bug#512318, and Bug#513864 seems to be related to that one.

If you want to target Lenny and you don't have Etch in your sources.list, pin stable at a higher priority than testing. This means that the pin automatically migrates once Lenny becomes stable (which happens hopefully in 2 weeks).
