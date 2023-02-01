---
title: "Ubuntu 2022v1 secure boot key rotation and friends"
date: 2023-02-01T14:40:27+01:00
copyright: 2023 Canonical Ltd
---

This is the story of the currently progressing changes to secure boot
on Ubuntu and the history of how we got to where we are.

# taking a step back: how does secure boot on Ubuntu work?

Booting on Ubuntu involves three components after the firmware:

1. shim
2. grub
3. linux

Each of these is a PE binary signed with a key. The shim is signed by Microsoft's
3rd party key and embeds a self-signed Canonical CA certificate, and optionally a
vendor dbx (a list of revoked certificates or binaries). grub and linux (and fwupd)
are then signed by a certificate issued by that CA

In Ubuntu's case, the CA certificate is sharded: Multiple people each have a part
of the key and they need to meet to be able to combine it and sign things, such as
new code signing certificates.

## BootHole

When BootHole happened in 2020, travel was suspended and we hence could not rotate
to a new signing certificate. So when it came to updating our shim for the CVEs, we
had to revoke all previously signed kernels, grubs, shims, fwupds by their hashes.

This generated a very large vendor dbx which caused lots of issues as shim exported
them to a UEFI variable, and not everyone had enough space for such large variables.
Sigh.

We decided we want to rotate our signing key next time.

This was also when upstream added SBAT metadata to shim and grub. This gives
a simple versioning scheme for security updates and easy revocation using a
simple EFI variable that shim writes to and reads from.

## Spring 2022 CVEs

We still were not ready for travel in 2021, but during BootHole we developed the
SBAT mechanism, so one could revoke a grub or shim by setting a single EFI variable.

We actually missed rotating the shim this cycle as a new vulnerability was reported
immediately after it, and we decided to hold on to it.

## 2022 key rotation and the fall CVEs 

This caused some problems when the 2nd CVE round came, as we did not have a shim
with the latest SBAT level, and neither did a lot of others, so we ended up deciding
upstream to not bump the shim SBAT requirements just yet. Sigh.

Anyway, in October we were meeting again for the first time at a Canonical sprint,
and the shardholders got together and created three new signing keys: 2022v1, 2022v2,
and 2022v3. It took us until January before they were installed into the signing service
and PPAs setup to sign with them.

We also submitted a shim 15.7 with the old keys revoked which came back at around
the same time.

Now we were in a hurry. The 22.04.2 point release was scheduled for around middle
of February, and we had nothing signed with the new keys yet, but our new shim
which we need for the point release (so the point release media remains bootable
after the next round of CVEs), required new keys.

So how do we ensure that users have kernels, grubs, and fwupd signed with the
new key before we install the new shim?

## upgrade ordering

grub and fwupd are simple cases: For grub, we depend on the new version. We decided
to backport grub 2.06 to all releases (which moved focal and bionic up from 2.04), and
kept the versioning of the -signed packages the same across all releases, so we were
able to simply bump the Depends for grub to specify the new minimum version. For fwupd-efi,
we added Breaks.

(Actually, we also had a backport of the CVEs for 2.04 based grub, and we did publish that
for 20.04 signed with the old keys before backporting 2.06 to it.)

Kernels are a different story: There are about 60 kernels out there. My initial idea was
that we could just add Breaks for all of them. So our meta package linux-image-generic which
depends on linux-image-$(uname -r)-generic, we'd simply add Breaks: linux-image-generic (<< 5.19.0-31)
and then adjust those breaks for each series. This would have been super annoying, but
ultimately I figured this would be the safest option. This however caused concern, because
it could be that apt decides to remove the kernel metapackage.

I explored checking the kernels at runtime and aborting if we don't have a trusted
kernel in preinst. This ensures that if you try to upgrade shim without having a kernel,
it would fail to install. But this ultimately has a couple of issues:

1. It aborts the entire transaction at that point, so users will be unable to run
   `apt upgrade` until they have a recent kernel.
1. We cannot even guarantee that a kernel would be unpacked first. So even if you got
   a new kernel, apt/dpkg might attempt to unpack it first and then the preinst would fail
   because no kernel is present yet.

Ultimately we believed the danger to be too large given that no kernels had yet been released
to users. If we had kernels pushed out for 1-2 months already, this would have been a viable
choice.

So in the end, I ended up modifying the shim packaging to install both the latest shim *and*
the previous one, and an update-alternatives alternative to select between the two:

In it's post-installation maintainer script, shim-signed checks whether all kernels with a
version greater or equal to the running one are not revoked, and if so, it will setup the
latest alternative with priority 100 and the previous with a priority of 50.
If one or more of those kernels was signed with a revoked key, it will swap the priorities
around, so that the previous version is preferred.

Now this is fairly static, and we do want you to switch to the latest shim eventually, so
I also added hooks to the kernel install to trigger the shim-signed postinst script when
a new kernel is being installed. It will then update the alternatives based on the current
set of kernels, and if it now points to the latest shim, reinstall shim and grub to the
ESP.

Ultimately this means that once you install your 2nd non-revoked kernel, or you install
a non-revoked kernel and then reconfigure shim or the kernel, you will get the latest
shim. When you install your first non-revoked kernel, your currently booted kernel is
still revoked, so it's not upgraded immediately. This has a benefit in that you will
most likely have two kernels you can boot without disabling secure boot.

## regressions

Of course, the first version I uploaded had still some remaining hardcoded "shimx64"
in the scripts and so failed to install on arm64 where "shimaa64" is used. And if that
were not enough, I also forgot to include support for gzip compressed kernels there. 
Sigh, I need better testing infrastructure to be able to easily run arm64 tests as
well (I only tested the actual booting there, not the scripts).

shim-signed migrated to the release pocket in lunar fairly quickly, but this caused
images to stop working, because the new shim was installed into images, but no
kernel was available yet, so we had to demote it to proposed and block migration.
Despite all the work done for end users, we need to be careful to roll this out for
image building.

## another grub update for OOM issues.

We had two grubs to release: First there was the security update for the recent set
of CVEs, then there also was an OOM issue for large initrds which was blocking critical
OEM work.

We fixed the OOM issue by cherry-picking all 2.12 memory management patches, as well
as the red hat patches to the loader we take from there. This ended up a fairly large
patch set and I was hesitant to tie the security update to that, so I ended up pushing
the security update everywhere first, and then pushed the OOM fixes this week.

With the OOM patches, you should be able to boot initrds of between 400M and 1GB, it
also depends on the memory layout of your machine and your screen resolution and background
images. So OEM team had success testing 400MB irl, and I tested up to I think it was 1.2GB
in qemu, I ran out of FAT space then and stopped going higher :D

## am I using this yet?

The new signing keys are used in:

* shim-signed 1.54 on 22.10+, 1.51.3 on 22.04, 1.40.9 on 20.04, 1.37~18.04.13 on 18.04
* grub2-signed 1.187.2~ or newer (binary packages grub-efi-amd64-signed or grub-efi-arm64-signed),
   1.192 on 23.04.
* fwupd-signed 1.51~ or newer
* various linux updates. Check `apt changelog linux-image-unsigned-$(uname -r)` to see if
  ` Revoke & rotate to new signing key (LP: #2002812)` is mentioned in there to see if it
  signed with the new key.

If you were able to install shim-signed, your grub and fwupd-efi will have the correct
version as that is ensured by packaging. However your shim may still point to the old one.
To check which shim will be used by grub-install, you can check the status of the `shimx64.efi.signed`
or (on arm64) `shimaa64.efi.signed` alternative. The best link needs to point to the file ending in
latest:

```
$ update-alternatives --display shimx64.efi.signed
shimx64.efi.signed - auto mode
  link best version is /usr/lib/shim/shimx64.efi.signed.latest
  link currently points to /usr/lib/shim/shimx64.efi.signed.latest
  link shimx64.efi.signed is /usr/lib/shim/shimx64.efi.signed
/usr/lib/shim/shimx64.efi.signed.latest - priority 100
/usr/lib/shim/shimx64.efi.signed.previous - priority 50
```

If it does not, but you have installed a new kernel compatible with the new shim, you can
switch immediately to the new shim after rebooting into the kernel by running `dpkg-reconfigure
shim-signed`. You'll see in the output if the shim was updated, or you can check the output
of `update-alternatives` as you did above after the reconfiguration has finished.

For the out of memory issues in grub, you need grub2-signed 1.187.3~ (same binaries
as above).

## deep dive: uploading signed boot assets to Ubuntu

For each signed boot asset, we build one version in the latest stable release and the
development release. We then binary copy the built binaries from the latest stable release
to older stable releases. This process ensures two things: We know the next stable release
is able to build the assets and we also minimize the number of signed assets.

OK, I lied. For shim, we actually do not build in the development release but copy the
binaries upward from the latest stable, as each shim needs to go through external signing.


The entire workflow looks something like this:

1. Upload the unsigned package to one of the following “build” PPAs:
   - https://launchpad.net/~ubuntu-uefi-team/+archive/ubuntu/ppa for non-embargoed updates
   - https://launchpad.net/~ubuntu-security-embargoed-shared/+archive/ubuntu/grub2 for embargoed updates
2. Upload the signed package to the same PPA
3. For stable release uploads:
   - Copy the unsigned package back across all stable releases in the PPA
   - Upload the signed package for stable releases to the same PPA with `~<release>.1` appended to the version
4. Submit a request to canonical-signing-jobs to sign the uploads.

   The signing job helper copies the binary -unsigned packages to the primary-2022v1 PPA where they are
   signed, creating a signing tarball, then it copies the source package for the -signed package to the
   same PPA which then downloads the signing tarball during build and places the signed assets into
   the -signed deb.

   Resulting binaries will be placed into the proposed PPA: https://launchpad.net/~ubuntu-uefi-team/+archive/ubuntu/proposed

5. Review the binaries themselves
6. Unembargo and binary copy the binaries from the proposed PPA to the proposed-public PPA: https://launchpad.net/~ubuntu-uefi-team/+archive/ubuntu/proposed-public.

   This step is not strictly necessary, but it enables tools like sru-review to work, as they cannot access the packages from the normal private “proposed” PPA.
7. Binary copy from proposed-public to the proposed queue(s) in the primary archive

Lots of steps!

## WIP

As of writing, only the grub updates have been released, other updates are still being
verified in proposed. An update for fwupd in bionic will be issued at a later point, removing
the EFI bits from the fwupd 1.2 packaging and using the separate fwupd-efi project instead
like later release series. 
