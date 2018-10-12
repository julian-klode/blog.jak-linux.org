---
author: juliank
date: 2012-04-22 17:05:40+00:00
draft: false
title: Reference Counting and Tail Calls
type: post
url: /2012/04/22/reference-counting-and-tail-calls/
categories:
- General
---

One thing I thought about today is reference counting in combination with tail calls. Imagine a function like this:


    
    
    function f(x) { return g(x+1); }
    



Now consider that `x` is a reference counted object and that `x + 1` creates a new object. The call to `g(x + 1)` shall be in tail call position.

In most reference counted languages, the reference to an argument is owned by the caller. That is, `f()` owns the reference to `x + 1`. In that case, the call to `g()` would no longer be in a tail call position, as we still have to decrease the reference count after `g()` exits.

An alternative would be that the callee owns the reference. This however, will most likely create far more reference count changes than a caller-owns language (increase reference count in caller, decrease reference count in callee). For example, the following function requires an increment before the call to `g()`.


    
    
    function f1(x) { return g(x); }
    



Does anyone have any ideas on how to solve the problem of tail calls while avoiding the callee-owns scenario? Something that does not require a (non-reference-counting) garbage collector would be preferably.
