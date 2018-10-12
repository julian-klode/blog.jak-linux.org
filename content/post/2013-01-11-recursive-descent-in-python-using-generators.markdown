---
author: juliank
date: 2013-01-11 11:30:48+00:00
draft: false
title: Recursive-descent in Python, using generators
type: post
url: /2013/01/11/recursive-descent-in-python-using-generators/
categories:
- Python
---

Writing recursive descent parsers is easy, especially in Python (just like everything is easy in Python). But Python defines a low limit on the number of recursive calls that can be made, and recursive descent parsers are prone to exceed this limit.

We should thus write our parser without real recursion. Fortunately, Python offers us a way out: Coroutines,  introduced in Python 2.5 as per PEP 342. Using coroutines and a simple trampoline function, we can convert every mutually recursive set of functions into a set of coroutines that require constant stack space.

Let's say our parser looks like this (tokens being an iterator over characters):


    
    
    def parse(tokens):
        token = next(tokens)
        if token.isalnum():
            return token
        elif token == '(':
             result = parse(tokens)
             if next(tokens) != ')': raise ...
             return result
        else:
             raise ...
    



We now apply the following transformations:
          return X => yield (X)
          parse()  => (yield parse())

That is, we yield the value we want to return, and we yield a generator whenever we want to call (using a yield expression). Our rewritten parser reads:

    
    
    def parse(tokens):
        token = next(tokens)
        if token.isalnum():
            yield token
        elif token == '(':
             result = yield parse(tokens)
             if next(tokens) != ')': raise ...
             return result
        else:
             raise ...
    



We obviously cannot call that generator like the previous function. What we need to introduce is a trampoline. A trampoline is a function that manages that yielded generators, calls them, and passes their result upwards. It looks like this:


    
    
    def trampoline(generator):
        """Execute the generator using trampolining. """
        queue = collections.deque()
    
        def schedule(coroutine, stack=(), value=None):
            def resume():
                if 0:
                    global prev
                    now = stack_len(stack)
                    if now < prev:
                        print("Length", now)
                        prev = -1
                    elif prev != -1:
                        prev = now
                result = coroutine.send(value)
                if isinstance(result, types.GeneratorType):     # Normal call
                    schedule(result, (coroutine, stack))
                elif isinstance(result, Tail):                  # Tail call (if you want to)
                    schedule(result.value, stack)
                elif stack:                                     # Return to parent
                    schedule(stack[0], stack[1], result)
                else:                                           # Final Return
                    return result
    
            queue.append(resume)
    
        schedule(generator)
    
        result = None
        while queue:
            func = queue.popleft()
            result = func()
    
        return result
    



This function is based on the code in PEP 342, the difference being that 



  * we do not correctly propagate exceptions through the stack, but directly unwind to the caller of the parser (we don't handle exceptions inside our parser generators anyway)
  * the code actually compiles (code in PEP used 'value = coroutine.send(value)' which does not work)
  * the code returns a value (code in PEP was missing a return in schedule)
  * we don't use a class, and allow only one function to be scheduled at once (yes, we could get rid of the queue)
  * we allow tail calls [where Tail = namedtuple("Tail", ["result"])] to save some more memory.


For a more generic version of that, you might want to re-add exception passing, but the exceptions will then have long tracebacks, so I'm not sure how well they will work if you have deep recursion.

Now, the advantage of that is that our parser now requires constant stack space, because the actual real stack is stored in the heap using tuples which are used like singly-linked lists in scheme here. So, the only recursion limit is  available memory.

A disadvantage of that transformation is that the code will run slightly slower for small inputs that could be handled using a normally recursive parser.
