---
author: juliank
date: 2008-04-29 17:42:25+00:00
draft: false
title: 'Python Speed: ''x in list'' vs ''x in set'''
type: post
url: /2008/04/29/python-speed-x-in-list-vs-x-in-set/
categories:
- Python
---

Well, this is my second post about speed in Python. Today, I noticed that debimg's dependency resolver was much much slower than before. I thought what the problem could be and finally realized that the problem was that I switched from sets to list. This is fixed now in [commit d0fd700080de5c19cb5fd66918d14c5ffa26e805](http://git.debian.org/?p=users/jak-guest/debimg.git;a=commit;h=d0fd700080de5c19cb5fd66918d14c5ffa26e805)

Now, some benchmarks (using IPython):

In [1]: a = range(10**6)

In [2]: b = set(a)

In [3]: %timeit 10**6 in a
10 loops, best of 3: 31.8 ms per loop

In [4]: %timeit 10**6 in b
10000000 loops, best of 3: 98.6 ns per loop

1ms are 1 million ns. Therefore, using sets is about 322515 times faster than using lists (or tuples).

debimg can now calculate dependencies in 0.5 seconds again, instead of 1 minute with lists.
