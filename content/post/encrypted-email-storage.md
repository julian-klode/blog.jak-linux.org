---
title: "Encrypted Email Storage, or DIY ProtonMail"
date: 2019-06-13T22:47:11+02:00
---

In the [previous post]({{<ref "./setting-up-an-email-server-part1" >}}) about setting up a
email server, I explained how I setup a forwarder using Postfix. This post will look at setting
up Dovecot to store emails (and provide IMAP and authentication) on the server using GPG encryption
to make sure intruders can't read our precious data!

## Architecture

The basic architecture chosen for encrypted storage is that every incoming email is delivered
to postfix via LMTP, and then postfix runs a sieve script that invokes a filter that encrypts the email with
PGP/MIME using a user-specific key, before processing it further. Or short:

``` 
postfix --ltmp--> dovecot --sieve--> filter --> gpg --> inbox
```

Security analysis:
This means that the message will be on the system unencrypted as long as it is in a Postfix
queue. This further means that the message plain text should be recoverable for quite some
time after Postfix deleted it, by investigating in the file system. However, given enough time,
the probability of being able to recover the messages should reduce substantially. Not sure how
to improve this much.

And yes, if the email is already encrypted we're going to encrypt it a second time, because
we can nest encryption and signature as much as we want! Makes the code easier.

## Encrypting an email with PGP/MIME

PGP/MIME is a trivial way to encrypt an email. Basically, we take the entire email message,
armor-encrypt it with GPG, and stuff it into a multipart mime message with the same headers
as the second attachment; the first attachment is a control information.

Technically, this means that we keep headers twice, once encrypted and once decrypted. But
the advantage compared to doing it more like most normal clients is clear: The code is a lot
easier, and we can reverse the encryption and get back the original!

And when I say easy, I mean easy - the function to encrypt the email is just a few lines long:
```python3
def encrypt(message: email.message.Message, recipients: typing.List[str]) -> str:
    """Encrypt given message"""
    encrypted_content = gnupg.GPG().encrypt(message.as_string(), recipients)
    if not encrypted_content:
        raise ValueError(encrypted_content.status)

    # Build the parts
    enc = email.mime.application.MIMEApplication(
        _data=str(encrypted_content).encode(),
        _subtype='octet-stream',
        _encoder=email.encoders.encode_7or8bit)

    control = email.mime.application.MIMEApplication(
        _data=b'Version: 1\n',
        _subtype='pgp-encrypted; name="msg.asc"',
        _encoder=email.encoders.encode_7or8bit)
    control['Content-Disposition'] = 'inline; filename="msg.asc"'

    # Put the parts together
    encmsg = email.mime.multipart.MIMEMultipart(
        'encrypted',
        protocol='application/pgp-encrypted')
    encmsg.attach(control)
    encmsg.attach(enc)

    # Copy headers
    headers_not_to_override = {key.lower() for key in encmsg.keys()}

    for key, value in message.items():
        if key.lower() not in headers_not_to_override:
            encmsg[key] = value

    return encmsg.as_string()
```

Decypting the email is even easier: Just pass the entire thing
to GPG, it will decrypt the encrypted part, which, as mentioned,
contains the entire original email with all headers :)

```python3
def decrypt(message: email.message.Message) -> str:
    """Decrypt the given message"""
    return str(gnupg.GPG().decrypt(message.as_string()))
```

(now, not sure if it's a feature that GPG.decrypt ignores any
unencrypted data in the input, but well, that's GPG for you).

Of course, if you don't actually need IMAP access, you could drop
PGP/MIME and just pipe emails through `gpg --encrypt --armor` before
dropping them _somewhere_ on the filesystem, and then sync them via
ssh somehow (e.g. patching `maildirsync` to encrypt emails it uploads
to the server, and decrypting emails it downloads).

### Pretty Easy privacy (p≡p)
Now, we _almost_ have a file conforming to 
[draft-marques-pep-email-02](https://tools.ietf.org/html/draft-marques-pep-email-02),
the Pretty Easy privacy (p≡p) format, version 2. 
That format allows us to encrypt headers, thus preventing people from
snooping on our metadata!

Basically it relies on the fact that we have all the headers in the
inner (encrypted) message. To mark an email as conforming to that
format we just have to set the subject to p≡p and add a header describing
the format version:
```
       Subject: =?utf-8?Q?p=E2=89=A1p?=
       X-Pep-Version: 2.0
```

A client conforming to p≡p will, when seeing this email, read any
headers from the inner (encrypted) message.

We also might want to change the code to only copy a limited amount of
headers, instead of basically every header, but I'm going to leave that
as an exercise for the reader.


## Putting it together

Assume we have a Postfix and a Dovecot configured, and a script
`gpgmymail` written using the function above, like this:

```
def main() -> None:
    """Program entry"""
    parser = argparse.ArgumentParser(
        description="Encrypt/Decrypt mail using GPG/MIME")
    parser.add_argument('-d', '--decrypt', action="store_true",
                        help="Decrypt rather than encrypt")
    parser.add_argument('recipient', nargs='*',
                        help="key id or email of keys to encrypt for")
    args = parser.parse_args()
    msg = email.message_from_file(sys.stdin)

    if args.decrypt:
        sys.stdout.write(decrypt(msg))
    else:
        sys.stdout.write(encrypt(msg, args.recipient))


if __name__ == '__main__':
    main()
```

(don't forget to add missing imports, or see the end of the blog
post for links to full source code)

Then, all we have to is edit our `.dovecot.sieve` to add

```
filter "gpgmymail" "myemail@myserver.example";
```

and all incoming emails are automatically encrypted.

## Outgoing emails

To handle outgoing emails, do not store them via IMAP, but instead
configure your client to add a `Bcc` to yourself, and then filter
that _somehow_ in sieve. You probably want to set Bcc to something
like `myemail+sent@myserver.example`, and then filter on the detail
(the `sent`).

## Encrypt or not Encrypt?

Now do you actually want to encrypt? The disadvantages are clear:

*   Server-side search becomes useless, especially if you use p≡p with encrypted Subject.

    Such a shame, you could have built your own GMail by writing a notmuch FTS plugin for dovecot!

*   You can't train your spam filter via IMAP, because the spam trainer won't be able
    to decrypt the email it is supposed to learn from


There are probably other things I have not thought about, so
let me know on mastodon, email, or IRC!


## More source code
You can find the source code of the script, and the setup for
dovecot in my [git repository](https://github.com/julian-klode/ansible.jak-linux.org/compare/dovecot).
