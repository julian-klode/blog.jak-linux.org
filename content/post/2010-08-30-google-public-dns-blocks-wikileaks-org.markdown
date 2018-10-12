---
author: juliank
date: 2010-08-30 13:12:34+00:00
draft: false
title: 'Google Public DNS blocks wikileaks.org (Update: No, they don''t)'
type: post
url: /2010/08/30/google-public-dns-blocks-wikileaks-org/
categories:
- General
---

It seems that Google is blocking wikileaks.org in its 'Public DNS' servers (8.8.8.8 and 8.8.4.4):

    
    
    <div id="_mcePaste">; <<>> DiG 9.7.1-P2 <<>> @8.8.8.8 wikileaks.org
    ; (1 server found)
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 50227
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 0
    
    ;; QUESTION SECTION:
    ;wikileaks.org.			IN	A
    
    ;; Query time: 2457 msec
    ;; SERVER: 8.8.8.8#53(8.8.8.8)
    ;; WHEN: Fri Aug 27 18:10:43 2010
    ;; MSG SIZE  rcvd: 31</div>


**Update:** Sorry Google, for me doubting you. As it turns out, you did no evil, you were just a bit slower than the others.
