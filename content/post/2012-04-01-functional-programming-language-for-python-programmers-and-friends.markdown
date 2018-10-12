---
author: juliank
date: 2012-04-01 16:33:17+00:00
draft: false
title: Functional programming language for Python programmers and friends
type: post
url: /2012/04/01/functional-programming-language-for-python-programmers-and-friends/
categories:
- General
tags:
- '42'
- functional
- functional programming
- mutable
- pure
- python
- unique
- uniqueness type system
---

Just for you, and this time in the Pythonesque rendering.

    
    module main:
        import std (range)
        import std.io (printf, IO)
    
        # print the Fahrenheit-Celcius table for fahr = 0, 20, ..., 300
        function main(mutable IO io):
            Int lower = 0    # lower bound
            Int upper = 300  # upper bound
            Int step = 20    # step
            for Int fahr in range(lower, upper, step):
                Double celcius = 5 * (fahr - 32) / 9
                std.io.printf(io, "%3d\t%6.1f\n", fahr, celcius)


It does not really look like it, but this language is purely functional. It represents side effects using unique types. If you declare a mutable parameter, you basically declare a unique input parameter and a unique output parameter.

I’m also giving you a list implementation

    
    module std.container.list:
    
        ## The standard singly-linked list type
        type List[E]:
            Nil                     ## empty list
            Node:
                E value             ## current value
                List[E] next        ## remaining list
     


_
_And yes, both languages should be able to be represented using the same abstract syntax tree. The only change is the replacement of the opening curly brace by a colon, the removal of the closing curly bracket and semicolons, the replacement of C-style comments with Python-style comments and the requirement of indentation; oh and the for statement gets a bit lighter as well.
