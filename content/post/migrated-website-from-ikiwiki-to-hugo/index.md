---
title: "Migrated website from ikiwiki to Hugo"
date: 2018-10-25T20:42:16+02:00
tags:
  - hugo
  - ikiwiki
---

So, I've been using ikiwiki for my website since 2011. At the time, I was hosting
the website on a tiny hosting package included in a DSL contract - nothing dynamic
possible, so a static site generator seemed like a good idea.
ikiwiki was a good social fit at the time, as it was packaged in Debian and developed
by a Debian Developer.

Today, I finished converting it to [Hugo](https://gohugo.io).

## Why?

I did not really have a huge problem with ikiwiki, but I recently converted my blog
from wordpress to hugo and it seemed to make sense to have one technology for both,
especially since I don't update the website very often and forget ikiwiki's special
things.

One thing that was somewhat annoying is that I built a custom ikiwiki plugin for the
menu in my template, so I had to clone it's repository into `~/.ikiwiki` every time, 
rather than having a self-contained website. Well, it was a submodule of my dotfiles
repo.

Another thing was that ikiwiki had a lot of git integration, and when you build your
site it tries to push things to git repositories and all sorts of weird stuff -- Hugo
just does one thing: It builds your page.

One thing that Hugo does a lot better than ikiwiki is the built-in server which allows
you to run `hugo server´ and get a local http URL you can open in the browser with
live-reload as you save files. Super convenient to check changes (and of course, for
writing this blog post)!

Also, in general, Hugo feels a lot more _modern_. ikiwiki is from 2006, Hugo is from
2013. Especially recent Hugo versions added quite a few features for asset management.

* Fingerprinting of assets like css (inserting hash into filename) - ikiwiki just contains
  its style in `style.css` (and your templates in other statically named files), so if you
  switch theming details, you could break things because the CSS the browser has cached does
  not match the CSS the page expects.
* Asset minification - Hugo can minimize CSS and JavaScript for you. This means browers have
  to fetch less data.
* Asset concatenation - Hugo can concatenate CSS and JavaScript. This allows you to serve
  only one file per type, reducing the number of round trips a client has to make.

There's also proper theming support, so you can easily clone a theme into the `themes/`
directory, or add it as a submodule like I do for my blog. But I don't use it for the
website yet.

Oh, and Hugo automatically generates `sitemap.xml` files for your website, teaching
search engines which pages exist and when they have been modified.

I also like that it's written in Go vs in Perl, but I think that's just another _more modern_
type of thing. Gotta keep up with the world!


## Basic conversion
The first part to the conversion was to split the repository of the website: ikiwiki
puts templates into a `templates/` subdirectory of the repository and mixes all other
content. Hugo on the other hand splits things into `content/` (where pages go),
`layouts` (page templates), and `static/` (other files).

The second part was to inject the frontmatter into the markdown files. See, ikiwiki
uses shortcuts like this to set up the title, and gets its dates from git:

```
[[!meta title="My page title"]]
```

on the other hand, Hugo uses frontmatter - some YAML at the beginning of the markdown,
and specifies the creation date in there:

```
---
title: "My page title"
date: Thu, 18 Oct 2018 21:36:18 +0200
---
```

You can also have `lastmod` in there when modifying it, but I set `enableGitInfo = true`
in config.toml so Hugo picks up the mtime from the git repo.

I wrote a [small script](ikiwiki-to-hugo.py) to automatize those steps, but it was obviously
not perfect (also, it inserted lastmod, which it should not have).

One thing it took me some time to figure out was that `index.mdown` needs to become
`_index.md` in the `content/` directory of Hugo, otherwise no pages below it are
rendered - not entirely obvious.

## The theme

Converting the template was surprisingly easy, it was just a matter of replacing
`<TMPL_VAR BASEURL>` and friends with `{ .Site.BaseURL }` and friends - the names
are basically the same, just sometimes there's `.Site` at the front of it.

Then I had to take care of the menu generation loop. I had my `bootmenu` plugin for ikiwiki which
allowed me to generate menus from the configuration file. The template for it looked like this:

```
<TMPL_LOOP BOOTMENU>
    <TMPL_IF FIRSTNAV>
        <li <TMPL_IF ACTIVE>class="active"</TMPL_IF>><a href="<TMPL_VAR URL>"><TMPL_VAR PAGE></a></li>
    </TMPL_IF>
</TMPL_LOOP>
```

I converted this to:

```
{{ $currentPage := . }}
{{ range .Site.Menus.main }}
    <li class="{{ if $currentPage.IsMenuCurrent "main" . }}active{{ end }}">
        <a href="{{ .URL }}">
            {{ .Pre | safeHTML }}
            <span>{{ .Name }}</span>
        </a>
        {{ .Post }}
    </li>
{{ end }}
```

this allowed me to configure my menu in config.toml like this:

```
[menu]

  [[menu.main]]
    name = "dh-autoreconf"
    url = "/projects/dh-autoreconf"
    weight = -110
```

I can also specify `pre` and `post` parts and a `right` menu, and I use `pre` and
`post` in the right menu to render a few icons before and after items, for example:


```
  [[menu.right]]
    pre = "<i class='fab fa-mastodon'></i>"
    post = "<i class='fas fa-external-link-alt'></i>"
    url = "https://mastodon.social/@juliank"
    name = "Mastodon"
    weight = -70
```

Setting `class="active"` on the menu item does not seem to work yet, though; I think
I need to find out the right code for that...

## Fixing up the details
Once I was done with that steps, the next stage was to convert ikiwiki *shortcodes*
to something hugo understands. This took 4 parts:

The first part was converting tables. In ikiwiki, tables look like this:

```
[[!table format=dsv data="""
Status|License|Language|Reference
Active|GPL-3+|Java|[github](https://github.com/julian-klode/dns66)
"""]]
```

The generated HTML table had the `class="table"` set, which the bootstrap framework
needs to render a nice table. Converting that to a straightforward markdown hugo table
did not work: Hugo did not add the class, so I had to convert pages with tables in them
to the `mmark` variant of markdown, which allows classes to be set like this `{.table}`,
so the end result then looked like this:

```
{.table}
Status|License|Language|Reference
------|-------|--------|---------
Active|GPL-3+|Java|[github](https://github.com/julian-klode/dns66)
```

I'll be able to get rid of this in the future by using the bootstrap sources and
then having `table` inherit `.table` properties, but this requires saas or less, and
I only have the CSS at the moment, so using mmark was slightly easier.

The second part was converting ikiwiki links like `[[MyPage]]` and `[[my title|MyPage]]`
to Markdown links. This was quite easy, the first one became `[MyPage](MyPage)` and 
the second one `[my title](my page)`.

The third part was converting custom shortcuts: I had `[[!lp <number>]]` to generate
a link `LP: #<number>` to the corresponding launchpad bug, and `[[!Closes <number>]]`
to generate `Closes: #<number>` links to the Debian bug tracker. I converted those
to normal markdown links, but I could have converted them to [Hugo shortcodes](https://gohugo.io/templates/shortcode-templates/).
But meh.

The fourth part was about converting some directory indexes I had. For example,
`[[!map pages="projects/dir2ogg/0.12/* and ! projects/dir2ogg/0.12/*/*"]]` generated
a list of all files in `projects/dir2ogg/0.12`. There was a very useful shortcode
for that posted on the Hugo documentation, I did [a variant of it](https://github.com/julian-klode/jak-linux.org/blob/f1d5e4d48046ff08d7612de5fa44e06b3c8c6be6/layouts/shortcodes/directoryindex.html) and then converted
pages like this to `{{</* directoryindex path="/static/projects/dir2ogg/0.12" pathURL="/projects/dir2ogg/0.12" */>}}`. As
a bonus, the new directory index also generates SHA256 hashes for all files!

## Further work
The website is using an old version of bootstrap, and the theme is not split out yet. I'm
not sure if I want to keep a bootstrap theme for the website, seeing as the blog theme is
Bulma-based - it would be easier to have both use bulma.

I also might want to update both the website and the blog by pushing to GitHub and then
using CI to build and push it. That would allow me to write blog posts when I don't have
my laptop with me. But I'm not sure, I might lose control if there's a breach at travis.

