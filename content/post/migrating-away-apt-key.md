---
title: "Migrating away from apt-key"
date: 2021-06-20T09:42:22+02:00
---

This is an edited copy of an email I sent to provide guidance to users of apt-key as to how to handle things in a post apt-key world.


The manual page already provides all you need to know for replacing `apt-key add` usage:
> Note: Instead of using this command a keyring should be placed directly in the /etc/apt/trusted.gpg.d/ directory with a descriptive name and either "gpg" or "asc" as file extension

So it's kind of surprising people need step by step instructions for how to copy/download a file into a directory.

I'll also discuss the alternative security snakeoil approach with signed-by that's become popular. Maybe we should not have added `signed-by`, people seem to forget that debs still run maintainer scripts as root.

Aside from this email, Debian users should look into `extrepo`, which manages curated external repositories for you.

## Direct translation
Assume you currently have:

	wget -qO- https://myrepo.example/myrepo.asc | sudo apt-key add –

To translate this directly for bionic and newer, you can use:

	sudo wget -qO /etc/apt/trusted.gpg.d/myrepo.asc https://myrepo.example/myrepo.asc

or to avoid downloading as root:

	wget -qO-  https://myrepo.example/myrepo.asc | sudo tee -a /etc/apt/trusted.gpg.d/myrepo.asc

Older (and all) releases only support unarmored files with an extension .gpg. If you care about them, provide one, and use

	sudo wget -qO /etc/apt/trusted.gpg.d/myrepo.gpg https://myrepo.example/myrepo.gpg

Some people will tell you to download the `.asc` and pipe it to `gpg --dearmor`, but `gpg` might not be installed, so really, just offer a `.gpg` one instead that is supported on all systems.

## Pretending to be safer by using signed-by

People say it's good practice to _not_ use `trusted.gpg.d` and install the file elsewhere and then refer to it from the `sources.list` entry
by using `signed-by=<path to the file>`. So this looks a lot safer, because now your key can't sign other unrelated repositories. In
practice, security increase is minimal, since package maintainer scripts run as root anyway. But I guess it's better for publicity :)

As an example, here are the instructions to install `signal-desktop` from signal.org. As mentioned, `gpg --dearmor` use in there is not a good idea, and I'd personally not tell people to modify `/usr` as it's supposed to be managed by the package manager, but we don't have an `/etc/apt/keyrings` or similar at the moment; it's fine though if the keyring is installed by the package.

	# NOTE: These instructions only work for 64 bit Debian-based
	# Linux distributions such as Ubuntu, Mint etc.

	# 1. Install our official public software signing key
	wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg
	cat signal-desktop-keyring.gpg | sudo tee -a /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null

	# 2. Add our repository to your list of repositories
	echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main' |\
	  sudo tee -a /etc/apt/sources.list.d/signal-xenial.list

	# 3. Update your package database and install signal
	sudo apt update && sudo apt install signal-desktop

I do wonder why they do `wget | gpg --dearmor`, pipe that into the file and then `cat | sudo tee` it, instead of having that all in one pipeline. Maybe they want nicer progress reporting.

## Scenario-specific guidance

We have three scenarios:

For system image building, shipping the key in `/etc/apt/trusted.gpg.d` seems reasonable to me; you are the vendor sort of, so it can be globally trusted.

Chrome-style debs and repository config debs: If you ship a deb, embedding the `sources.list.d` snippet (calling it `$myrepo.list`) and shipping a `$myrepo.gpg `in `/usr/share/keyrings` is the best approach. Whether you ship that in product debs aka `vscode`/`chromium` or provide a repository configuration deb (let's call it `myrepo-repo.deb`) and then tell people to run `apt update` followed by `apt install <package inside the repo>` depends on how many packages are in the repo, I guess.

Manual instructions (signal style): The third case, where you tell people to run `wget` themselves, I find tricky. 
As we see in signal, just stuffing keyring files into `/usr/share/keyrings` is popular, despite `/usr` supposed to be managed by the package manager.
We don't have another dir inside `/etc` (or `/usr/local`), so it's hard to suggest something else. 
There's no significant benefit from actually using `signed-by`, so it's kind of extra work for little gain, though.


## Addendum: Future work

This part is new, just for this blog post. Let's look at upcoming changes and how they make things easier.

### Bundled `.sources` files

Assuming I get my [merge request](https://salsa.debian.org/apt-team/apt/-/merge_requests/176) merged, the next version of APT (2.4/2.3.something) will do away with all the complexity and allow you to embed the key directly into a deb822 `.sources` file (which have been available for some time now):

	Types: deb
	URIs: https://myrepo.example/ https://myotherrepo.example/
	Suites: stable not-so-stable
	Components: main
	Signed-By:
	 -----BEGIN PGP PUBLIC KEY BLOCK-----
	 .
	 mDMEYCQjIxYJKwYBBAHaRw8BAQdAD/P5Nvvnvk66SxBBHDbhRml9ORg1WV5CvzKY
	 CuMfoIS0BmFiY2RlZoiQBBMWCgA4FiEErCIG1VhKWMWo2yfAREZd5NfO31cFAmAk
	 IyMCGyMFCwkIBwMFFQoJCAsFFgIDAQACHgECF4AACgkQREZd5NfO31fbOwD6ArzS
	 dM0Dkd5h2Ujy1b6KcAaVW9FOa5UNfJ9FFBtjLQEBAJ7UyWD3dZzhvlaAwunsk7DG
	 3bHcln8DMpIJVXht78sL
	 =IE0r
	 -----END PGP PUBLIC KEY BLOCK-----

Then you can just provide a `.sources` files to users, 
they place it into `sources.list.d,
and everything magically works

Probably adding a nice `apt add-source` command for it I guess.

Well, python-apt's `aptsources` package still does not support deb822 sources, and
never will, we'll need an `aptsources2` for that for backwards-compatibility reasons,
and then port `software-properties` and other users to it.

### OpenPGP vs aptsign

We do have a better, tighter replacement for gpg in the works which uses Ed25519
keys to sign Release files. It's temporarily named `aptsign`, but it's a generic
signer for single-section deb822 files, similar to `signify`/`minisign`.

- Reference implementation: https://salsa.debian.org/apt-team/python-aptsign
- Specification: https://wiki.debian.org/Teams/Apt/Spec/AptSign

We believe that this solves the security nightmare that our OpenPGP integration
is while reducing complexity at the same time. Keys are much shorter, so the
bundled sources file above will look much nicer.
