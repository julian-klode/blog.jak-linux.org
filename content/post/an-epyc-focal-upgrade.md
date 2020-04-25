---
title: "An - EPYC - Focal Upgrade"
date: 2020-04-25T21:28:04+02:00
---

Ubuntu "Focal Fossa" 20.04 was released two days ago, so I took the opportunity yesterday
and this morning to upgrade my VPS from Ubuntu 18.04 to 20.04. The VPS provides:

- SMTP via Postfix
- Spam filtering via rspamd
- HTTP(S) via nginx and letsencrypt (certbot)
- Weechat relay
- OpenVPN server
- Shadowsocks proxy
- Unbound recursive DNS resolver, for the spam filtering

I rebooted one more time than necessary, though, as my cloud provider
[Hetzner](https://www.hetzner.de/cloud)
recently started offering 2nd generation EPYC instances which I upgraded to
from my Skylake Xeon based instance. I switched from the CX21 for 5.83€/mo
to the CPX11 for 4.15€/mo. This involved a RAM downgrade - from 4GB to 2GB,
but that's fine, the maximum usage I saw was about 1.3 GB when running
dose-distcheck (running hourly); and it's good for everyone that AMD is
giving Intel some good competition, I think.

Anyway, to get back to the distribution upgrade - it was fairly boring. I
started yesterday by taking a copy of the server and launching it locally
in a lxd container, and then tested the upgrade in there; to make sure I'm
prepared for the real thing :)

I got a confusing prompt from postfix as to which site I'm operating
(which is a normal prompt, but I don't know why I see it on an upgrade);
and a few config files I had changed locally.

As the server is managed by ansible, I just installed the distribution
config files and dropped my changes (setting `DPkg::Options { "--force-confnew"; };"` in apt.conf),
and then after the upgrade, ran ansible to redeploy the changes (after checking
what changes it would do and adjusting a few things).

There are two remaining flaws:

1. I run rspamd from the upstream repository, and that's not built for focal
   yet. So I'm still using the bionic binary, and have to keep bionic's icu 60
   and libhyperscan4 around for it.

   This is still preventing CI of the ansible config from passing for focal,
   because it won't have the needed bionic packages around.

2. I run weechat from the upstream repository, and apt can't tell the versions
   apart. Well, it can for the repositories, because they have `Size` fields -
   but `status` does not. Hence, it merges the installed version with the
   first repository it sees.

   What happens is that it installs from weechat.org, but then it believes the installed version
   is from archive.ubuntu.com and replaces it each dist-upgrade.

   I worked around it by moving the weechat.org repo to the front of sources.list,
   so that the it gets merged with that instead of the archive.ubuntu.com one, as
   it should be, but that's a bit ugly.

I also should start the migration to EC certificates for TLS, and 0-RTT handshakes,
so that the initial visit experience is faster. I guess I'll have to move away
from certbot for that, but I have not investigated this recently.
