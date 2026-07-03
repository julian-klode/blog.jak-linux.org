---
title: "The pandemic of incomplete OpenSSL error handling"
date: 2026-07-03T17:54:22+02:00
---

Recently a person reported a bug in APT saying that TLS is failing on FIPS
systems with MD5 errors, and suggested we call `ERR_clear_error()` around
TLS operations.

Like any serious software engineer would do, I said No. Just because one component
failed to handle its errors does not mean I can go around and discard all errors
in another place - the program should have failed earlier (or discarded the error
when it was determined to be safe).

Little did I know that people have for years been using this approach as a best
practice: Codebases everywhere are littered with calls to `ERR_clear_error()`
before performing TLS, and upstream themselves suggest to do just that.

This is a major, systemic, pandemic of incomplete error handling. We cannot
just discard unrelated errors if they become inconvenient. The code that
caused the error needs to be fixed to handle it.

This isn't all. It seems many authors are not familiar with libraries using a
stack of errors, and there is a second anti-pattern:

Call an OpenSSL operation, check the top-level error, and then discard all
errors if deemed "not too bad". This has the same problem: Unrelated errors
get silently discarded.

I would strongly encourage everyone to inspect their code bases for any calls
to `ERR_clear_error()` and whether they are safe or one of the bad patterns
above (or maybe you find a new pattern). You may want to use error stack
functionality of`ERR_set_mark` (https://docs.openssl.org/3.4/man3/ERR_set_mark/)
to essentially "push" and "pop" an error context of your own as a guard around
multiple OpenSSL operations.

To the OpenSSL authors, I would suggest not encouraging devastating security
practices that fundamentally break any trust in software.

We need to do better than this.
