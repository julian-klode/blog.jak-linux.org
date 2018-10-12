---
author: juliank
date: 2009-12-15 19:44:53+00:00
draft: false
title: The previous post
type: post
url: /2009/12/15/the-previous-post/
categories:
- APT2
---

Well, it seems that several news sites ([golem.de](http://www.golem.de/0912/71903.html), [pro-linux.de](http://www.pro-linux.de/news/2009/15080.html), [linux-magazin.de](http://www.linux-magazin.de/NEWS/Apt2-beschleunigt-Paketsuche), [linux-magazine.com](http://www.linux-magazine.com/Online/News/APT2-to-Accelerate-Debian-Package-Installation), [ubuntu-user.de](http://www.ubuntu-user.de/Online/News/Apt2-soll-die-Installation-von-Debian-Paketen-beschleunigen) [the last ones all from the same publishing house]), especially German ones have picked up the last blog post with same false impressions.

First, they stated that I am planning an APT2 release for Christmas.  They took the statement


<blockquote>[...] the internal branch has seen a lot of new code[...]. Most of the code will need to be reworked before it will be published, but I hope to have this completed until Christmas. </blockquote>


as a proof for this. But in the context of this paragraph, 'publish' was not meant in the term of publishing a release, but in the term of publishing the code (of the internal branch) in the public repository. The code is public now and lives in a 'temp' branch and will be reworked there for inclusion in the master branch.

Secondly, those news sites called me an Ubuntu developer. While I do contribute to Ubuntu, and am an Ubuntu Member, I am NOT an Ubuntu Developer, as I am NOT a member of the relevant ubuntu-dev team at launchpad.

Thirdly, those who stated that speed is a goal (mostly pro-linux, at least from my understanding): It is not, at least not now. It is just a coincidence caused by using a relational database. Furthermore, the test was not really fair, since the other package managers both provide more information than capt; information which has yet to be made accessible in APT2. It was just an initial conclusion that SQLite is quite fast.

Please note that APT2 is a free time project in development, and the programming language used is still in development as well; as well as some other reverse dependencies. I should also state that neither Debian nor Ubuntu have any plans to drop apt at the moment; and APT is still actively developed. 
