---
title: "New blog, new world"
date: 2018-10-11T21:45:14+02:00
---

(Test draft)

Back in May or so, when the GDPR happened, I disabled access to my blog
on https://juliank.wordpress.com, with the intention of migrating the blog
to my own site.

The day has finally come, and here is a new blog! The blog is static html
rendered by Hugo, and there are comments retrieved from replies on 
[Mastodon](https://joinmastodon.org), specifically the [mastodon.social](https://mastodon.social)
instance.

After pushing a new blog entry, a tool generates a new post on Mastodon announcing it, and
replies to that post will be shown as comments on the webpage. The comments are fetched from
mastodon.io on the server side, but avatars are fetched directly from the Mastodon server at
the moment.

Full source code is available on [github.com/julian-klode/blog.jak-linux.org](https://github.com/julian-klode/blog.jak-linux.org)
