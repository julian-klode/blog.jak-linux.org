---
author: juliank
date: 2010-07-09 11:22:36+00:00
draft: false
title: Build systems
type: post
url: /2010/07/09/build-systems/
categories:
- General
---

In the past weeks, I was looking at several build systems. As it turned out, there is not a single sane generic build system out there.

**Autotools**: Autotools are ugly, slow, and require an immense amount of code copies in the source tree.

**WAF**: WAF is not as ugly as autools and it's faster and does not generate Makefiles or stuff like this. But it has serious issues: It requires one to copy it to the source tarball, has no stable API, and requires Python for building. Furthermore, support for unit testing is broken: It runs the unit tests, but does not abort the build process if the tests fail and does not display why the tests fail.

**CMake**: The syntax is ugly, it generates Makefiles, and support for pkg-config seems to be very very basic.

So how should a build system look like?



	  * It should be installed in the system and not require code copies in the source tree (and thus no pre-build actions)
	  * It should not generate Makefiles, but build the project itself.
	  * It should not require more than a standard C library.
	  * It should support pkg-config out of the box.
	  * It should support SONAMEs for libraries.
	  * It should detect dependencies on headers automatically.
	  * It should support unit testing and abort if the tests fail.
	  * It should not require developers to specify how to do things, only what to do.

So, why is there no sane build system?
