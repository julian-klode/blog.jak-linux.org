---
author: juliank
date: 2012-04-01 15:41:17+00:00
draft: false
title: '[updated] Functional programming language for C programmers and friends'
type: post
url: /2012/04/01/mutable-types-and-functional-programming/
categories:
- General
tags:
- '42'
- C
- functional
- functional programming
- mutable
- pure
- unique
- uniqueness type system
---

Just for you:


    
    module main {
        import std (range);
        import std.io (printf, IO);
     
        /* print the Fahrenheit-Celcius table
            for fahr = 0, 20, ..., 300 */
        function main(mutable IO io) {
            Int lower = 0;   // lower bound
            Int upper = 300; // upper bound
            Int step = 20;   // step
            for (Int fahr in range(lower, upper, step)) {
                Double celcius = 5 * (fahr - 32) / 9;
                std.io.printf(io, "%3d\t%6.1f\n", fahr, celcius);
            }
        }
    }



It does not really look like it, but this language is purely functional. It represents side effects using unique types. If you declare a mutable parameter, you basically declare a unique input parameter and a unique output parameter.

I'm also giving you a list implementation


    
    
    module std.container.list {
    
        /** The standard singly-linked list type */
        type List[E] {
            Nil;                    /** empty list */
            Node {
                E value;            /** current value */
                List[E] next;       /** remaining list */
            }
        }
    }
    



Thus are only excerpts from a document with tens of pages and the reference implementation of the standard library. The incomplete working draft for the language is attached: [JAK Programming Language Early Working Draft (28 pages)](https://juliank.files.wordpress.com/2012/04/jlang1.pdf).

**Update:** Fixed the link.
