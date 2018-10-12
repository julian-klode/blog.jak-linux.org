---
author: juliank
date: 2009-06-05 18:34:53+00:00
draft: false
title: python-apt 0.7.91 released
type: post
url: /2009/06/05/python-apt-0-7-91-released/
categories:
- Debian
- Ubuntu
---

As I promised, I released python-apt 0.7.91 today. This version provides a new API, with real classes in apt_pkg, new names which conform to PEP 8 conventions, and it supports new language features such as the 'with' statement. Old code should still continue to work, if it does not and it is using only public interfaces, report a bug against python-apt or send an email.

I can not guarantee that all the names will be kept like they are at the moment (it's a pre-release), but there should not be many more changes needed. The series will hit Ubuntu Karmic later this month, and the final 0.8.0 release is going to be shipped in the final Karmic release.

If you want to help with python-apt, consider to write some examples of what can be done with python-apt, and some tutorials for the documentation. You can also check for spelling mistakes and alike. If you want, you can also contribute code. See the documentation (in the package, or [online](http://apt.alioth.debian.org/python-apt-doc-exp/)) for guidelines on how to contribute.

You can get the 0.7.91 release from Debian experimental, and you can view the documentation online at [http://apt.alioth.debian.org/python-apt-doc-exp/](http://apt.alioth.debian.org/python-apt-doc-exp/).

And of course, a short example:

    
    
    with cache.actiongroup(): # apt.Cache 'cache'
        for package in my_selected_packages:
            package.mark_install() # New PEP 8 names, previously named markInstall()
    



