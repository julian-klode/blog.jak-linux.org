---
title: "APT Patterns"
date: 2019-08-15T15:55:47+02:00
draft: true
---

If you have ever used aptitude a bit more extensively on the command-line, you'll probably have come across its patterns. This week I spent some time implementing (some) patterns for apt, so you do not need aptitude for that, and I want to let you in on the details of this [merge request !74](https://salsa.debian.org/apt-team/apt/merge_requests/74).

## what are patterns

Patterns allow you to specify complex search queries to select the packages you want to install/show. 
For example, the pattern `?garbage` can be used to find all packages that have been automatically installed but are no longer depended upon by manually installed packages.
Or the pattern `?automatic` allows you find all automatically installed packages.

You can make this more complex by combining patterns, for example,
`?and(?automatic,?obsolete)` matches all automatically installed packages not longer in a repository.

There are also explicit targets, so you can query stuff like `?for x: ?depends(?recommends(x))` which finds you all packages `x` that depend on another package that recommends `x`. 
I do not fully comprehend those yet - I did not manage to create a pattern that matches all manually installed packages that a metapackage depends upon. I am not sure it is possible.

## reducing pattern syntax

aptitude's syntax for patterns is heavily context-sensitive. If you have a pattern `?foo(?bar)` it can have two possible meanings:

1.  If `?foo` takes arguments (like `depends` did), then `?bar` is the argument.
2.  Otherwise, `?foo(?bar)` is equivalent to `?foo?bar` which is short for `?and(?foo,?bar)`

There are other shorthands too. For example, you could write `~c` instead of config-files, or `~m` for automatic; then combine them like `~m~c`.

I find that very confusing. When looking at implementing patterns in APT, I went for a different approach. 
I first parse the pattern into a generic parse tree, without knowing anything about the semantics, and then I convert the parse tree into a `APT::CacheFilter::Matcher`, an object that can match against packages. 
I also only implemented long patterns, not short ones (or concatenation for `?and`).

So in our example above, `?foo(?bar)` cannot mean `?foo?bar` as we 

1. do not support concatenation for `?and`. 
2. automatically parse `(` as the argument list, no matter whether `?foo` supports arguments or not

This is useful, because the syntactic structure of the pattern can be seen, without having to know which patterns have arguments and which do not.

That said, the second pass knows whether a pattern accepts arguments or not and insists on you adding them if required and not having them if it does not accept any.

{{< figure src="/2019/08/15/apt-patterns/parser-error.png" caption="apt not understanding invalid patterns" >}}

## Supported syntax

At the moment, APT supports two kinds of patterns: Basic logic ones like `?and`, and patterns that apply to an entire package as opposed to a specific version. 
This was done as a starting point for the merge, patterns for versions will come in the next round.

We also do not have any support for explicit search targets yet - as explained, I do not yet fully understand them, and hence do not want to commit on them.

The full list of the first round of patterns is below, helpfully converted from docbook to markdown by pandoc.

### logic patterns

These patterns provide the basic means to combine other patterns into
more complex expressions, as well as `?true` and `?false` patterns.

`?and(PATTERN, PATTERN, ...)`

:   Selects objects where all specified patterns match.

`?false`

:   Selects nothing.

`?not(PATTERN)`

:   Selects objects where PATTERN does not match.

`?or(PATTERN, PATTERN, ...)`

:   Selects objects where at least one of the specified patterns match.

`?true`

:   Selects all objects.

### package patterns

These patterns select specific packages.

`?architecture(WILDCARD)`

:   Selects packages matching the specified architecture, which may
    contain wildcards using any.

`?automatic`

:   Selects packages that were installed automatically.

`?broken`

:   Selects packages that have broken dependencies.

`?config-files`

:   Selects packages that are not fully installed, but have solely
    residual configuration files left.

`?essential`

:   Selects packages that have Essential: yes set in their control file.

`?exact-name(NAME)`

:   Selects packages with the exact specified name.

`?garbage`

:   Selects packages that can be removed automatically.

`?installed`

:   Selects packages that are currently installed.

`?name(REGEX)`

:   Selects packages where the name matches the given regular
    expression.

`?obsolete`

:   Selects packages that no longer exist in repositories.

`?upgradable`

:   Selects packages that can be upgraded (have a newer candidate).

`?virtual`

:   Selects all virtual packages; that is packages without a version.
    These exist when they are referenced somewhere in the archive, for
    example because something depends on that name.

## examples

`apt remove ?garbage`

:   Remove all packages that are automatically installed and no longer
    needed - same as apt autoremove

`apt purge ?config-files`

:   Purge all packages that only have configuration files left

## oddities

Some things are not yet where I want them:

-  `?architecture` does not support `all`, `native`, or `same`
-  `?installed` should match only the installed version of the package, not the entire package (that is what aptitude does, and it's a bit surprising that `?installed` impl)


## the future

Of course, I do want to add support for the missing version patterns and explicit search patterns. I might even add support for some of the short patterns, but no promises. Some of those explicit search patterns might have _slightly_ different syntax, e.g. `?for(x, y)` instead of `?for x: y` in order to make the language more uniform and easier to parse.

Another thing I want to do ASAP is to disable fallback to regular expressions when specifying package names on the command-line: `apt install g++` should always look for a package called `g++`, and not for any package containing `g` (`g++` being a valid regex) when there is no `g++` package. I think continuing to allow regular expressions if they start with `^` or end with `$` is fine - that prevents any overlap with package names, and would avoid breaking most stuff.

There also is the fallback to `fnmatch()`: Currently, if apt cannot find a package with the specified name using the exact name or the regex, it would fall back to interpreting the argument as a `glob(7)` pattern. For example, `apt install apt*` would fallback to installing every package starting with `apt` if there is no package matching that as a regular expression. We can actually keep those in place, as the `glob(7)` syntax does not overlap with valid package names.

Maybe I should allow using `[]` instead of `()` so larger patterns become more readable, and/or some support for comments.