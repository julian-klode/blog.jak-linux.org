---
author: juliank
date: 2016-09-25 18:22:43+00:00
draft: false
title: Introducing TrieHash, a order-preserving minimal perfect hash function generator
  for C(++)
type: post
url: /2016/09/25/introducing-triehash-a-order-preserving-minimal-perfect-hash-function-generator-for-c/
categories:
- General
---

## Abstract


I introduce TrieHash an algorithm for constructing perfect hash functions from tries. The generated hash functions are pure C code, minimal, order-preserving and outperform existing alternatives. Together with the generated header files,they can also be used as a generic string to enumeration mapper (enums are created by the tool).


## Introduction


APT (and dpkg) spend a lot of time in parsing various files, especially Packages files. APT currently uses a function called AlphaHash which hashes the last 8 bytes of a word in a case-insensitive manner to hash fields in those files (dpkg just compares strings in an array of structs).

There is one obvious drawback to using a normal hash function: When we want to access the data in the hash table, we have to hash the key again, causing us to hash every accessed key at least twice. It turned out that this affects something like 5 to 10% of the cache generation performance.

Enter perfect hash functions: A perfect hash function matches a set of words to constant values without collisions. You can thus just use the index to index into your hash table directly, and do not have to hash again (if you generate the function at compile time and store key constants) or handle collision resolution.

As #debian-apt people know, I happened to play a bit around with tries this week before guillem suggested perfect hashing. Let me tell you one thing: My trie implementation was very naive, that did not really improve things a lot...


## Enter TrieHash


Now, how is this related to hashing? The answer is simple: I wrote a perfect hash function generator that is based on tries. You give it a list of words, it puts them in a trie, and generates C code out of it, using recursive switch statements (see code generation below). The function achieves competitive performance with other hash functions, it even usually outperforms them.

Given a dictionary, it generates an enumeration (a C `enum` or C++ `enum class`) of all words in the dictionary, with the values corresponding to the order in the dictionary (the order-preserving property), and a function mapping strings to members of that enumeration.

By default, the first word is considered to be 0 and each word increases a counter by one (that is, it generates a minimal hash function). You can tweak that however:

    
    = 0
    WordLabel ~ Word
    OtherWord = 9
    


will return 0 for an unknown value, map "Word" to the enum member `WordLabel` and map OtherWord to 9. That is, the input list functions like the body of a C enumeration. If no label is specified for a word, it will be generated from the word. For more details see the documentation


### C code generation



    
    switch(string[0] | 32) {
    case 't':
        switch(string[1] | 32) {
        case 'a':
            switch(string[2] | 32) {
            case 'g':
                return Tag;
            }
        }
    }
    return Unknown;


Yes, really recursive switches - they directly represent the trie. Now, we did not really do a straightforward translation, there are some optimisations to make the whole thing faster and easier to look at:

First of all, the `32` you see is used to make the check case insensitive in case all cases of the switch body are alphabetical characters. If there are non-alphabetical characters, it will generate two cases per character, one upper case and one lowercase (with one break in it). I did not know that lowercase and uppercase characters differed by only one bit before, thanks to the clang compiler for pointing that out in its generated assembler code!

Secondly, we only insert breaks only between cases. Initially, each case ended with a return Unknown, but guillem (the dpkg developer) suggested it might be faster to let them fallthrough where possible. Turns out it was not faster on a good compiler, but it's still more readable anywhere.

Finally, we build one trie per word length, and switch by the word length first. Like the 32 trick, his gives a huge improvement in performance.


## Digging into the assembler code


The whole code translates to roughly 4 instructions per byte:

  1. A memory load,
  2. an or with 32
  3. a comparison, and
  4. a conditional jump.

(On x86, the case sensitive version actually only has a cmp-with-memory and a conditional jump).

Due to [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77729](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=77729) this may be one instruction more: On some architectures an unneeded zero-extend-byte instruction is inserted - this causes a 20% performance loss.


## Performance evaluation


I run the hash against all 82 words understood by APT in Packages and Sources files, 1,000,000 times for each word, and summed up the average run-time:

<table>
  <tr>
    <td>host</td>
    <td>arch</td>
    <td>Trie</td>
    <td>TrieCase</td>
    <td>GPerfCase</td>
    <td>GPerf</td>
    <td>DJB</td>
  </tr>
  <tbody>
    <tr>
      <td>plummer</td>
      <td>ppc64el</td>
      <td>540</td>
      <td>601</td>
      <td>1914</td>
      <td>2000</td>
      <td>1345</td>
    </tr>
    <tr>
      <td>eller</td>
      <td>mipsel</td>
      <td>4728</td>
      <td>5255</td>
      <td>12018</td>
      <td>7837</td>
      <td>4087</td>
    </tr>
    <tr>
      <td>asachi</td>
      <td>arm64</td>
      <td>1000</td>
      <td>1603</td>
      <td>4333</td>
      <td>2401</td>
      <td>1625</td>
    </tr>
    <tr>
      <td>asachi</td>
      <td>armhf</td>
      <td>1230</td>
      <td>1350</td>
      <td>5593</td>
      <td>5002</td>
      <td>1784</td>
    </tr>
    <tr>
      <td>barriere</td>
      <td>amd64</td>
      <td>689</td>
      <td>950</td>
      <td>3218</td>
      <td>1982</td>
      <td>1776</td>
    </tr>
    <tr>
      <td>x230</td>
      <td>amd64</td>
      <td>465</td>
      <td>504</td>
      <td>1200</td>
      <td>837</td>
      <td>693</td>
    </tr>
  </tbody>
</table>

Suffice to say, GPerf does not really come close.

All hosts except the x230 are Debian porterboxes. The x230 is my laptop with a a Core i5-3320M, barriere has an Opteron 23xx. I included the DJB hash function for another reference.


## Source code


The generator is written in Perl, licensed under the MIT license and available from [https://github.com/julian-klode/triehash](https://github.com/julian-klode/triehash) - I initially prototyped it in Python, but guillem complained that this would add new build dependencies to dpkg, so I rewrote it in Perl.

Benchmark is available from [https://github.com/julian-klode/hashbench](https://github.com/julian-klode/hashbench)


## Usage


See the script for POD documentation.
