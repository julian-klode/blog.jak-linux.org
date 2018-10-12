---
author: juliank
date: 2014-01-06 16:46:41+00:00
draft: false
title: python-apt now native Python 3 code
type: post
url: /2014/01/06/python-apt-now-native-python-3-code/
categories:
- Debian
- Python
---

Today I made an important change to the python-apt code: It is now native Python 3 code (but also works under Python 2). The previous versions all run 2to3 during the build process to create a Python 3 version. This is no longer needed, as the code is now identical.

As part of that change, python-apt now only supports Python 2.7, Python 3.3, and newer. I'm using some features only present in 3.3 like Python2 unicode literal syntax in order to keep the code simple.

Here's how I did it:

I took the Python 2 code and ran 2to3 -f print -x future on it. This turned every print statement in a call to the print function. I then went ahead and added a "from __future__ import print_function" to the top of each module. This was the first commit.

For the second commit, I ran 2to3 -p -x future to convert the remaining stuff to Python 3, and then undid some changes (like unicode literals) and fixed the rest of the changes to work under both Python 2 and 3. Sometimes I added a top-level code like:


    
    
    if sys.version_info_major >= 3:
        unicode = str
    



So I could use unicode in the code for the Python 2 cases.

I used various backported modules like io and stuff only available in Python 2.7, so dropped support for Python 2.6.
