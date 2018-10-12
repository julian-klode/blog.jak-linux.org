---
author: juliank
date: 2014-10-14 21:46:03+00:00
draft: false
title: Key transition
type: post
url: /2014/10/14/key-transition/
---

I started transitioning from 1024D to 4096R.  The new key is available at:

https://people.debian.org/~jak/pubkey.gpg

and the keys.gnupg.net key server. A very short transition statement is available at:

https://people.debian.org/~jak/transition-statement.txt

and included below (the http version might get extended over time if needed).

The key consists of one master key and 3 sub keys (signing, encryption, authentication). The sub keys are stored on an OpenPGP v2 Smartcard. That's really cool, isn't it?

Somehow it seems that GnuPG 1.4.18 also works with 4096R keys on this smartcard (I accidentally used it instead of gpg2 and it worked fine), although only GPG 2.0.13 and newer is supposed to work.


    
    
    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA1,SHA512
    
    Because 1024D keys are not deemed secure enough anymore, I switched to
    a 4096R one.
    
    The old key will continue to be valid for some time, but i prefer all
    future correspondence to come to the new one.  I would also like this
    new key to be re-integrated into the web of trust.  This message is
    signed by both keys to certify the transition.
    
    the old key was:
    
    pub   1024D/00823EC2 2007-04-12
          Key fingerprint = D9D9 754A 4BBA 2E7D 0A0A  C024 AC2A 5FFE 0082 3EC2
    
    And the new key is:
    
    pub   4096R/6B031B00 2014-10-14 [expires: 2017-10-13]
          Key fingerprint = AEE1 C8AA AAF0 B768 4019  C546 021B 361B 6B03 1B00
    
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2
    
    iEYEARECAAYFAlQ9j+oACgkQrCpf/gCCPsKskgCgiRn7DoP5RASkaZZjpop9P8aG
    zhgAnjHeE8BXvTSkr7hccNb2tZsnqlTaiQIcBAEBCgAGBQJUPY/qAAoJENc8OeVl
    gLOGZiMP/1MHubKmA8aGDj8Ow5Uo4lkzp+A89vJqgbm9bjVrfjDHZQIdebYfWrjr
    RQzXdbIHnILYnUfYaOHUzMxpBHya3rFu6xbfKesR+jzQf8gxFXoBY7OQVL4Ycyss
    4Y++g9m4Lqm+IDyIhhDNY6mtFU9e3CkljI52p/CIqM7eUyBfyRJDRfeh6c40Pfx2
    AlNyFe+9JzYG1i3YG96Z8bKiVK5GpvyKWiggo08r3oqGvWyROYY9E4nLM9OJu8EL
    GuSNDCRJOhfnegWqKq+BRZUXA2wbTG0f8AxAuetdo6MKmVmHGcHxpIGFHqxO1QhV
    VM7VpMj+bxcevJ50BO5kylRrptlUugTaJ6il/o5sfgy1FdXGlgWCsIwmja2Z/fQr
    ycnqrtMVVYfln9IwDODItHx3hSwRoHnUxLWq8yY8gyx+//geZ0BROonXVy1YEo9a
    PDplOF1HKlaFAHv+Zq8wDWT8Lt1H2EecRFN+hov3+lU74ylnogZLS+bA7tqrjig0
    bZfCo7i9Z7ag4GvLWY5PvN4fbws/5Yz9L8I4CnrqCUtzJg4vyA44Kpo8iuQsIrhz
    CKDnsoehxS95YjiJcbL0Y63Ed4mkSaibUKfoYObv/k61XmBCNkmNAAuRwzV7d5q2
    /w3bSTB0O7FHcCxFDnn+tiLwgiTEQDYAP9nN97uibSUCbf98wl3/
    =VRZJ
    -----END PGP SIGNATURE-----
    
