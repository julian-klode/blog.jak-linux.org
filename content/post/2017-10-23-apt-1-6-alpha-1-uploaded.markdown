---
author: juliank
date: 2017-10-23 00:44:01+00:00
draft: false
title: APT 1.6 alpha 1 - seccomp and more
type: post
url: /2017/10/23/apt-1-6-alpha-1-uploaded/
---

I just uploaded APT 1.6 alpha 1, introducing a very scary thing: Seccomp sandboxing for methods, the programs downloading files from the internet and decompressing or compressing stuff. With seccomp I reduced the number of system calls these methods can use to 149 from 430. Specifically we excluded most ways of IPC, xattrs, and most importantly, the ability for methods to `clone(2)`, `fork(2)`, `execve(2)`, and `execveat(2)`. Yes, that's right - methods can no longer execute programs.

This was a real problem, because the http method did in fact execute programs - there is this small option called `ProxyAutoDetect` or `Proxy-Auto-Detect` where you can specify a script to run for an URL and the script outputs a (list of) proxies. In order to be able to seccomp the http method, I moved the invocation of the script to the parent process. The parent process now executes the script within the sandbox user, but without seccomp (obviously).

I tested the code on amd64, ppc64el, s390x, arm64, mipsel, i386, and armhf. I hope it works on all other architectures libseccomp is currently built for in Debian, but I did not check that, so your apt might be broken now if you use powerpc, powerpcspe, armel, mips, mips64el, hhpa, or x32 (I don't think you can even really use x32).

Also, apt-transport-https is gone for good now. When installing the new apt release, any installed apt-transport-https package is removed (apt breaks apt-transport-https now, but it also provides it versioned, so any dependencies should still be satisfiable).

David also did a few cool bug fixes again, finally teaching apt-key to ignore unsupported GPG key files instead of causing weird errors :)
