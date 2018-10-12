---
author: juliank
date: 2008-04-02 17:33:50+00:00
draft: false
title: Python Extension for libisofs
type: post
url: /2008/04/02/python-extension-for-libisofs/
categories:
- Debian
- Python
---

I am working on a Python extension for the libisofs library. The extension is written in [Cython](http://www.cython.org/) , a Python-like language designed to write Python extensions.

At a later point, this extension will be used to create the ISO Images in debimg. It will be disabled by default, but you can enable it via a configuration option.
