---
author: juliank
date: 2011-05-11 16:52:57+00:00
draft: false
title: 'Project APT2: new cache format and small things'
type: post
url: /2011/05/11/project-apt2-new-cache-format-and-small-things/
categories:
- APT2
---

I did not write much code or merge much of my prototype code, but some things happened since the last blog post about APT2 specific things in August and I forgot to write about them.

First of all, I dropped the GVariant-based cache. The format strings were simply getting ugly long and were not very understandable, performance was just much too slow (needing more than a few nanoseconds for a package lookup is obviously too slow for solving dependency problems); furthermore, building the cache was also slow and complicated because we needed all attributes of an object at once to pass them to GVariant, leading to ugly API.

I replaced the GVariant cache with one that can be easily mmap()ed and is described completely in C. It's derived from APT's cache design (but more robust, as it includes the size of the cache and we can thus detect to small files, although that's scheduled for the next ABI break in APT as well), but has fewer duplicate data, and uses arrays where APT uses linked lists. The reason for arrays is simple: They take up less space and can be represented naturally in Python and other languages using array-based lists. The cache also contains a coalesced hash table which does use a linked list, but that one is a bit different, as it is for searching only and not exposed. Everything non-stringy is 64-bit aligned in order to keep things as simple as possible. All integers are fixed size, thus the format is architecture-independent if you fix byte orders. The format is described at [http://people.debian.org/~jak/apt2-doc/apt-Cache-Format.html](http://people.debian.org/~jak/apt2-doc/apt-Cache-Format.html).

I stole one more idea from cupt and changed the configuration system to verify types of variables. APT2's configuration system knows more types than cupt's, though, including regular expressions, directory and filenames (i.e. it does not let you store a value /d/ in a file variable), strings (which store everything), unsigned and signed integers, and boolean options; all of which are checked when parsing files (producing warnings) or command-line options (producing errors).

I have also simplified the type world by removing all iterator types except for one, replacing them with `get_thing()` and `n_things()` functions in the objects holding the arrays. Makes cool bindings slightly harder, but makes the C API much easier to use from C.

Most things expected from a package manager are still missing, but what is there looks good in most cases (especially `AptConfiguration` has a nice API, and no complaints from valgrind anywhere). Currently I am working on Python bindings so I can interact with the functions easily and check things in an interactive fashion; and I am also writing a document explaining the concepts behind APT2, drafts at [http://people.debian.org/~jak/midlevel.pdf](http://people.debian.org/~jak/midlevel.pdf). I also have some more code pending further thoughts (including complete index parsing), but it might still take some time before I have something usable in the wild.

On other package managers: From time to time I also use Cupt, look at Cupt code, hack Cupt code, and report bugs against Cupt. I still do not really understand the (extreme) nesting of directory structures in the source code, why there are so (extremely) many source files split all over them, or the general concepts of Cupt, but I can hack together what I need for my personal testing. I also play with yum whenever I end up on a Fedora system (which happens from time to time).
