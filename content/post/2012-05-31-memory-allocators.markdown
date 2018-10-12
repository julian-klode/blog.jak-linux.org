---
author: juliank
date: 2012-05-31 09:43:00+00:00
draft: false
title: Memory allocators
type: post
url: /2012/05/31/memory-allocators/
categories:
- General
---

In the past days, I looked at various memory allocators in a quest to improve performance in my multi-threaded test cases of a reference counting language runtime / object allocator (a fun project).

It turns out the glibc's memory allocator is relatively slow, especially if you do loops that create one element and destroy one element at the same time (for example, map() on a list you no longer use after you passed it to map). To fix this problem, I considered various options.

The first option was to add a thread-local cache around malloc(). So whenever we want to free() an object, we place it on  a thread-local list instead, and if a malloc() request for an object of that size comes in, we reuse the old object. 

This fixes the problem with the lists, but experiments shown another problem with the glibc allocator: Allocating many objects without releasing others (let's say appending an element to a functional list). I started testing with tcmalloc instead, and noticed that it was several times faster (reducing run time from 6.75 seconds to 1.33 seconds (5 times faster)). As I do not want to depend on a C++ code base, I decided to write a simple allocator that allocates blocks of memory via mmap(), splits those into objects, and puts the objects on a local free list. That allocator performed faster than tcmalloc(), but was also just a simple test case, and not really useable, due to potential fragmentation problems (and because the code was statically linked in, causing thread-local storage to be considerably faster, as it does not need to call a function on every TLS access, but can rather go through a segment register).

I then discovered jemalloc, and tried testing with this. It turned out that jemalloc was even faster than tcmalloc in all test cases, and also required about the same amount of memory as tcmalloc (and slightly more than the custom test code, as that combined reference counting with memory allocator metadata and thus had less meta data overhead). Using jemalloc, the list building test performs in 0.9X seconds now (instead of tcmalloc's 1.33 or glibc's 6.75 seconds), requires 0 major page faults (tcmalloc has 2), and uses 5361472 kb memory (tcmalloc uses 5290240, glibc requires 7866608).

Given that jemalloc is written in C, I can only recommend it to everyone in need of a scalable memory allocator. Depending on your workload, it might require less memory than tcmalloc (at least that's the case at Facebook) and is most likely faster than tcmalloc. It also provides tcmalloc-compatible profiling facilities (as Facebook needed them). Furthermore, jemalloc is also the memory allocator used by FreeBSD, and is used by Mozilla projects, and on several Facebook projects, and should thus be relatively stable and useable.

All tests were run with 4 threads, on a dual-core laptop with hyper-threading, using (e)glibc 2.13, tcmalloc 2.0, and jemalloc 3.0. The tests may not be representative of real world performance, and do not account for fragmentation.

Should I try replacing Python's custom caching of malloc() calls with simply calling jemalloc, and run a few Python benchmarks? Anyone interested in that?
