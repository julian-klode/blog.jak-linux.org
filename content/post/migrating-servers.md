---
title: "Migrating web servers"
date: 2018-12-01T23:40:21+01:00
---

As of today, I migrated various services from shared hosting on
uberspace.de to a VPS hosted by [hetzner](https://www.hetzner.de).
This includes my weechat client, this blog, and the following other
websites:

- jak-linux.org
- dep.debian.net redirector
- mirror.fail

## Rationale
Uberspace runs CentOS 6. This was causing more and more issues for me,
as I was trying to run up-to-date weechat binaries. In the final stages,
I ran weechat and tmux inside a debian proot. It certainly beat compiling
half a system with linuxbrew.

The web performance was suboptimal. Webpages are served with Pound and Apache,
TLS connection overhead was just huge, there was only HTTP/1.1, and no
keep-alive.

Security-wise things were interesting: Everything ran as my user, obviously,
whether that's scripts, weechat, or mail delivery helpers. Ugh. There was
also only a single certificate, meaning that all domains shared it, even
if they were completely distinct like jak-linux.org and dep.debian.net

## Enter Hetzner VPS
I launched a VPS at hetzner and configured it with Ubuntu 18.04, the
latest Ubuntu LTS.  It is a CX21, so it has 2 vcores, 4 GB RAM, 40 GB
SSD storage, and 20 TB of traffic. For 5.83€/mo, you can't complain.

I went on to build a repository of ansible roles (see [repo on github.com](https://github.com/julian-klode/ansible.jak-linux.org)),
that configured the system with a few key characteristics:

- http is served by nginx
- certificates are per logical domain - each domain has a canonical name
  and a set of aliases; and the certificate is generated for them all
- HTTPS is configured according to Mozilla's modern profile, meaning
  TLSv1.2-only, and a very restricted list of ciphers. I can revisit that
  if it's causing problems, but I've not seen huge issues.
- Log files are anonymized to 24 bits for IPv4 addresses, and 32 bit for
  IPv6 addresses, which should allow me to identify an ISP, but not an
  individual user.

I don't think the roles are particularly reusable for others, but it's
nice to have a central repository containing all the configuration for
the server.

## Go server to serve comments

When I started self-hosting the blog and added commenting via mastodon,
it was via a third-party PHP script. This has been replaced by a Go
program ([GitHub repo](https://github.com/julian-klode/mastodon-comments)).
The new Go program scales a lot better than a PHP script, and provides
better security properties due to AppArmor and systemd-based sandboxing;
it even uses systemd's DynamicUser.

Special care has been taken to have time outs for talking to upstream
servers, so the program cannot hang with open connections and will
respond eventually.

The Go binary is connected to nginx via a UNIX domain socket that
serves FastCGI. The service is activated via systemd socket activation,
allowing it to be owned by www-data, while the binary runs as a dynamic
user. Nginx's native fastcgi caching mechanism is enabled so
the Go process is only contacted every 10 minutes at the most (for a given
post). Nice!


## Performance
Performance is a lot better than the old shared server. Pages load
in up to half the time of the old one. Scalability also seems better:
I tried various benchmarks, and achieved consistently higher concurrency
ratings. A simple curl via https now takes 100ms instead of 200ms.

Performance is still suboptimal from the west coast of the US or other
places far away from Germany, but got a lot better than before:
Measuring from Oregon using webpagetest, it took 1.5s  for a page to
fully render vs ~3.4s before. A CDN would surely be faster, but would
lose the end-to-end encryption.

## Upcoming mail server
The next step is to enable email. Setting up postfix with dovecot
is quite easy it turns out. Install them, tweak a few settings, setup
SPF, DKIM, DMARC, and a PTR record, and off you go.

I mostly expect to read my email by tagging it on the server using
notmuch somehow, and then syncing it to my laptop using muchsync. The
IMAP access should allow some notifications or reading on the phone.

Spam filtering will be handled with [rspamd](https://rspamd.com). It
seems to be the hot new thing on the market, is integrated with postfix
as a milter, and handles a lot of stuff, such as:

- greylisting
- IP scoring
- DKIM verification and signing
- ARC verification
- SPF verification
- DNS lists
- Rate limiting

It also has fancy stuff like neural networks. Woohoo!

As another bonus point: It's trivial to confine with AppArmor, which
I really love. Postfix and Dovecot are a mess to confine with their
hundreds of different binaries.

I found it via uberspace, which plan on using it for their next
uberspace7 generation. It is also used by some large installations
like rambler.ru and locaweb.com.br.


I plan to migrate mail from uberspace in the upcoming weeks, and will
post more details about it.
