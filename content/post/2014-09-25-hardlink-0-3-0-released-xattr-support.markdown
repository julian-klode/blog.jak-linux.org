---
author: juliank
date: 2014-09-25 12:41:47+00:00
draft: false
title: hardlink 0.3.0 released; xattr support
type: post
url: /2014/09/25/hardlink-0-3-0-released-xattr-support/
---

Today I not only submitted my bachelor thesis to the printing company, I also released a new version of hardlink, my file deduplication tool.

hardlink 0.3 now features support for xattr support, contributed by Tom Keel at Intel. If this does not work correctly, please blame him.

I also added support for a --minimum-size option.

Most of the other code has been tested since the upload of RC1 to experimental in September 2012.

The next major version will split up the code into multiple files and clean it up a bit. It's getting a bit long now in a single file.
