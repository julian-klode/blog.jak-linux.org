---
author: juliank
date: 2011-05-11 16:05:28+00:00
draft: false
title: underscores and undefined behavior
type: post
url: /2011/05/11/underscores-and-undefined-behavior/
categories:
- General
---

As everyone should know, underscores in C are not cool, as they cause undefined behavior per 7.1.3:



<blockquote>
All identifiers that begin with an underscore and either an uppercase letter or another underscore are always reserved for any use.
[...]
If the program declares or defines an identifier in a context in which it is reserved (other than as allowed by 7.1.4), or defines a reserved identifier as a macro name, the behavior is undefined.
</blockquote>



Yet, they are widely used everywhere. Here are some examples:



	  * inclusion guards in GLib: ` __G_VARIANT_H__`
          * internal Python functions: `_PyUnicode_AsString`
          * various macros in APT: `__deprecated`, `__hot`


All of this triggers undefined behavior and is thus uncool. Of course in APT, it's most stupid, as we do not have any namespace and could thus 
end up redefining things we should not much more likely then the other two.

But why were those solutions chosen in the first place, and what is the alternative? I cannot answer the first question, but for the second one, the obvious alternative is to use trailing underscores:


	  * inclusion guards, defined behavior: ` G_VARIANT_H__`
          * internal functions, defined behavior: `PyUnicode_AsString_`
          * various macros, defined behavior: `deprecated__`, `hot__`


Then there is another class of reserved identifiers with underscores:



<blockquote>
All identifiers that begin with an underscore are always reserved for use as identifiers
with file scope in both the ordinary and tag name spaces.
</blockquote>



Meaning that everything except for parameters, local variables and members of structs/unions that starts with an underscore is reserved. So, if you happen to create a variable `_mylibrary_debug_flag`, you trigger undefined behavior as well. And while we're at it, do not think you can create a type ending in `_t`: POSIX reserves all identifiers ending in `_t` for its own use.

In summary, whenever you write C and want to be 100% safe of undefined-behavior-because-of-naming, do not start any identifier with an underscore and do not end any identifier with `_t`.
