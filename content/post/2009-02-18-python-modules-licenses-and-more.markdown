---
author: juliank
date: 2009-02-18 17:27:11+00:00
draft: false
title: Python modules, licenses, and more
type: post
url: /2009/02/18/python-modules-licenses-and-more/
categories:
- General
---

Today, I want to present you some things I have asked myself and some ideas about them. You should not expect the information to be correct. Therefore, if you find mistakes, please leave a comment.


## Copyright statements / Comments


MIT license: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. - If you had a python module released under the MIT license, and this is in the comment of the module and you somehow ship only pyc or pyo files, you would be violating the license by not including the copyright notice, because these files do not contain the modules. This is also true for many other licenses, but this seems to be the best example.

If you include this in the docstrings, you would only violate such license terms if you distribute bytecode created with the -OO option. This also does not apply if the code is a program which prints the license (eg. via a commandline --license option).


## GPL vs LGPL


Is there any difference at all? The LGPL requires you to publish all changes you make to the code, while the GPL also requires you to publish source files you have created. This also means that you can't link a non-free program to a GPL library, but you can link it to a LGPL library.

Because Python modules are not linked to each other, everything you do is normally considered a use of the module. Therefore, if there is a module G released under the GPL, and a module X released under a different, incompatible license X, you would still be able to use the facilities provided by the module G. This also effects subclassing classes of G in X.

Due to the enormous flexibility provided by Python you can easily break the intented rules of the GPL. Instead of editing the class definition you subclass the class and edit it. You can also replace stuff inside the module G during run-time, simply by setting the relevant attributes.

In summary, Python makes it very easy to work around the restrictions of the GPL, therefore, using the LGPL instead of the GPL makes no sense. You can't give others more rights than they already have. You would just make it easier for others in case they want to write new code and want to copy some of yours.


## What about the AGPL?


The AGPL exposes (compared to the GPL3) further restrictions on using the software on eg. websites. It is intended for programs which may be used by SaaS providers. Like with the GPL, the enormous flexibility of Python compensates most of the restrictions the license.


## BTW, which license to choose?


I normally choose to release my programs and modules, etc. under the terms of the GNU General Public License, version 3 (or at your option) any later version. But it also depends on the size of the project. When I work on small scripts, like hardlink, I generally choose the MIT license. This is also somehow related to the fact that I don't want to have a license which takes more than 50% of the size of my project.

This is actually a bit different to what Bruce Perens [does](http://itmanagement.earthweb.com/osrc/article.php/12068_3803101_2/Bruce-Perens-How-Many-Open-Source-Licenses-Do-You-Need.htm). Bruce recommends 3 types of licenses. The first one is what he calls the "gift" license. He recommends the Apache License 2.0, because it provides better "protection from software patent lawsuites". The MIT license is another example for this type of license. While not providing the patent protection, this is not that critical for persons like me who live in Germany. Furthermore, the number of patents possibly infringed by the code is proportional to the amount of code.

The second type he recommends is a "sharing-with-rules" license, like the GPL 3. Like him, I mostly use this license for my code. Sometimes I also use the GPL 2, but only when I am required to do so, or because of tradition. In generally, I only upgrade software from GPL-2+ to GPL-3+ when I introduce new features, not for bug fixes or similar.

The third type he describes is the "in-between license", like the LGPL. As I pointed out above, this type of license is not much different than the GPL, at least if applied to Python modules. Therefore, I never release any Python module under such a license. Things may be different for C libraries (and others), but I never released one.


## Documentation, etc.


Well, I license all my documentation under the same license as the software. This makes it easier for the user because he does not need to read yet another license (at least if he reads all the licenses of the software he uses). If I distribute non-code content independent of code, I generally choose a Creative Commons License (CC-BY-SA 3.0, CC-BY 3.0), Germany.

This also has an effect on this blog. From now on, all content (ever) provided by me via this blog is licensed under the terms of the [Creative Commons Attribution-Share Alike 3.0 Germany](http://creativecommons.org/licenses/by-sa/3.0/de/), unless a different license information is included as part of the post. The design and comments from other persons are not included.


## Why I wrote this


Really, I don't know. Maybe I just want to write something, maybe I want to write these things down, so I can read them. Anyway, please tell me if I my conclusions/ideas are wrong.

**Update 1:** There was a mistake "should expect the information to be correct", fixed now: "should not expect [...]". I may be wrong with the GPL vs. LGPL thing, have not completely checked this. _(2009-02-18 19:18 CET)_

**Update 2**: Seems the GPL vs LGPL thing is not correct, as written by "Anonymous" and Bruce. _(2009-02-18 19:26 CET)_
