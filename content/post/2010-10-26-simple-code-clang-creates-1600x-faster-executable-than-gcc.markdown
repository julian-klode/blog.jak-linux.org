---
author: juliank
date: 2010-10-26 13:58:38+00:00
draft: false
title: simple code - clang creates 1600x faster executable than gcc
type: post
url: /2010/10/26/simple-code-clang-creates-1600x-faster-executable-than-gcc/
categories:
- General
---

The following program, compiled with clang 1.1, runs 500 times faster than the gcc4.5-compiled code (in both cases with -O2):

    
    <span style="color:#008200;">#include <stdio.h></span>
    
    <span style="color:#008200;">#define len 1000000000L</span>
    
    <span style="color:#830000;">unsigned long</span> <span style="color:#010181;">f</span><span style="color:#000000;">(</span><span style="color:#830000;">unsigned long</span> a<span style="color:#000000;">,</span> <span style="color:#830000;">unsigned long</span> b<span style="color:#000000;">)</span> <span style="color:#010181;">__attribute__</span><span style="color:#000000;">((</span>noinline<span style="color:#000000;">));</span>
    
    <span style="color:#830000;">int</span> <span style="color:#010181;">main</span><span style="color:#000000;">()</span>
    <span style="color:#000000;">{</span>    
        <span style="color:#010181;">printf</span><span style="color:#000000;">(</span><span style="color:#ff0000;">"%lu</span><span style="color:#ff00ff;">\n</span><span style="color:#ff0000;">"</span><span style="color:#000000;">,</span> <span style="color:#010181;">f</span><span style="color:#000000;">(</span><span style="color:#2928ff;">0</span><span style="color:#000000;">,</span> <span style="color:#2928ff;">2</span><span style="color:#000000;">*</span>len<span style="color:#000000;">));</span>
        <span style="color:#000000;font-weight:bold;">return</span> <span style="color:#2928ff;">0</span><span style="color:#000000;">;</span>
    <span style="color:#000000;">}</span>
    
    <span style="color:#830000;">unsigned long</span> <span style="color:#010181;">f</span><span style="color:#000000;">(</span><span style="color:#830000;">unsigned long</span> a<span style="color:#000000;">,</span> <span style="color:#830000;">unsigned long</span> b<span style="color:#000000;">)</span>
    <span style="color:#000000;">{</span>
        <span style="color:#830000;">unsigned long</span> sum <span style="color:#000000;">=</span> <span style="color:#2928ff;">0</span><span style="color:#000000;">;</span>
        <span style="color:#000000;font-weight:bold;">for</span> <span style="color:#000000;">(;</span> a <span style="color:#000000;"><</span> b<span style="color:#000000;">;</span> a<span style="color:#000000;">++)</span>
            sum <span style="color:#000000;">+=</span> a<span style="color:#000000;">;</span>
        <span style="color:#000000;font-weight:bold;">return</span> sum<span style="color:#000000;">;</span>
    <span style="color:#000000;">}</span>
    



Now, I would be interested to see what's happening here. I took a look at the assembler code both compilers create, but the only thing I found out so far is that gcc's assembly is easier to understand - 50 lines (gcc) vs 134 lines (clang). If someone knows the answer, please tell me.

Also see [http://lwn.net/Articles/411776/](http://lwn.net/Articles/411776/) for a C++ version that calls `f()` via `boost::thread`.

Update: I also reported a bug at [http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46186](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=46186).
