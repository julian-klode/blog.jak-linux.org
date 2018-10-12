---
author: juliank
date: 2008-03-24 22:38:12+00:00
draft: false
title: 'Python Speed: Getting the first part of a string'
type: post
url: /2008/03/24/python-speed-getting-the-first-part-of-a-string/
categories:
- Python
---

If you want to get the first part of a string (in the following example a), you should use the partition method of the string, as it is the fastest way (and it also gives you the delimiter in [1] and the other part of the string in [2]):

In [1]: a = 'a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/q/r/s/t/u/v/w/x/y/z'

In [2]: timeit a.partition('/')[0]
1000000 loops, best of 3: 362 ns per loop

In [3]: timeit  a[:a.find('/')]
1000000 loops, best of 3: 443 ns per loop

In [4]: timeit a.split('/', 1)[0]
1000000 loops, best of 3: 697 ns per loop

In [5]: timeit a.split('/')[0]
1000000 loops, best of 3: 1.45 µs per loop

These tests were made with IPython 0.8.1 (Python 2.5.1 (r251:54863, Oct  5 2007, 13:50:07) ) on an Ubuntu 64 bit system.
