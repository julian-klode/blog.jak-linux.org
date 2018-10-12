---
author: juliank
date: 2009-01-04 00:03:09+00:00
draft: false
title: 'python-apt: Deprecation of mixedCase names, re-organisation of apt.progress,
  and more'
type: post
url: /2009/01/04/python-apt-deprecation-of-mixedcase-names-re-organisation-of-aptprogress-and-more/
categories:
- Debian
---

[as sent to deity@lists.debian.org]


**Hello**,





while hacking a bit on python-apt in the last days, I formulated some
proposals which I want to present to you.





I have already implemented proposals I and VII, started with the implementation
of proposal II, and have partially implemented proposal III, all in
my local branch. I could implement the rest next week, and this could
result in python-apt 0.7.9~exp2 (at least this is my wish, I do not
have commit access to the python-apt repository, and this mail is not
discussed yet:) ).





My local branch is not online yet, but I'm working on it. It is based
off debian-sid revision 202 (which is 0.7.9~exp1).





I would have also suggest to (at least partially) follow PEP 7 (C code),
but re-indenting the whole extension code is not a good idea.





Before I go on, I would like to know your opinions about these proposals,
what you like and what not, your suggestions, etc, etc...





## List of Proposals




    
    
     I   Deprecation of mixedCase naming conventions in apt module
     II  Re-organisation of the apt.progress module
     III Language updates
     IV  Unification of testing code
     V   Cleanup of the code
     VI  Using unique variable names throughout the modules
     VII Some other changes
     





## I. Deprecation of mixedCase naming conventions in apt module





In order to comply with PEP 8, we should start to change our names
from mixedCase to lowercase_with_underscores style. This style is
more common in the Python world, and used eg. in the Python library.





### I hereby propose that:






  1. a new module apt.deprecate is introduced, which provides functions
for compatibility and a class named DeprecateMixedCase
  2. Most classes are changed to subclass DeprecateMixedCase instead of
object.
  3. All methods, attributes and variable names are changed from the
mixedCase style to the lowercase_with_underscores style.
  4. apt_pkg will be changed to call the new methods on progress objects,
and fall back to the old names if methods with new names are not
available.




### How backward compatibility is implemented:





The DeprecatedMixedName class provides the methods **getattr**()
 and **setattr**(). These classes will forward all access to attributes
 with mixedNames to the ones with lowercase_with_underscores names.





In case of methods, the **getattr**() method returns a helper function
 which fixes all keyword arguments with mixedCase names and than calls
 the right function.





As this only works for methods with mixedCase names, methods which have
 mixedCase-named args, get the argument **kwds, and its content will be
 checked for mixedCase-named arguments. [On the other side, given that
 the API is marked as not stable, we could also drop that level of
 compatibility.]





### Schedule:






  1. Implement all the changes in an experimental version of python-apt
as soon as possible.
  2. (A) Once all packages have been adjusted to use the new names, remove
    the old ones (about 50 binary packages, and I would write the needed
    patches). This would Breaks: about 50 packages.
or
(B) After the release of Debian Squeeze, remove the compatibility
    functions (and the deprecate module from apt). This is the same
    as (A), but does not require Breaks on 50 packages.




### Known Issues:






  1. The methods will not be available using their oldName at class
level, only at object level. This means that some code subclassing
apt.* classes may fail. Most code will not break, however.




## II. Re-organisation of the apt.progress module





The apt.progress module is not very consistent in the way classes
are named. For example, there is OpTextProgress but TextFetchProgress.





### Therefore, I hereby propose that:






  1. For each of the for types of progress ('Cdrom', 'Fetch', 'Install', 'Op'),
a new class is introduced with the name: Abstract%sProgress % progress
  2. For each type of progress a class Text%sprogress % progress is introduced,
which subclasses Abstract%sProgress and provides textual output
  3. For further classes, a general naming scheme is introduced, which is
"%(output_type)s%(progress_type)sProgress" [whereas (1) and (2) implement
this naming scheme]




### Schedule:





Same as in proposal I.





## III. Language updates





The apt package has been written some time ago, and has not been updated
to make use of the latest language features.





### Therefore, I propose that:






  1. all code using old language features is adjusted to use language
features as of Python 2.5.
1.1 Examples include the use of decorators, and the use
    of str methods instead of functions of the string module.
  2. The with statement will be used where appropriate, and that
apt_pkg.*Lock() gain support for being used as context managers.




### Schedule:





Implement as soon as possible.





## IV. Unification of testing code





Most modules ship test code which will be called when the module is
run as a script.





### Therefore, I propose that:






  1. All testing code in the apt module is removed
  2. All the tests in the 'tests' directory of python-apt
are converted to a unified testing suite.
  3. Testing code which has been removed as part of (1) is
reintroduced in the relevant test module, if appropriate.




### Schedule:





Implement as soon as possible.





## V. Cleanup of the code





In accordance to PEP 8, which is also named as a rule in apt/README.apt,
code will be reformatted where needed.





This includes 2 lines between module-level definitions, spaces after
',', comparing to None using 'is' instead of '=', and more.





### Schedule:





Implement as soon as possible.





## VI. Using unique variable names throughout the modules





I hereby propose the following names:




    
    
     cache    - An apt.cache.Cache() object
     pkg      - An object returned by cache[str()] (in special cases)
     pkg      - An apt.package.Package() object
     cand     - An object returned by depcache.GetCandidateVer()
    





This would remove some confusion for developers, especially
if you see that apt.Package() objects are named cand in debfile,
but pkg everywhere else.





### Schedule:





Implement as soon as possible.





## VII. Some other changes





Here is a list of other changes I have already made in my branch:






  * Remove apt.package.Record(), it behaves exactly like the
object it is wrapping (apt_pkg.ParseTagFile() result)
  * Move the Origin class out of the Package() class and at
the module level.
  * If a package should be marked for upgrade, but is not upgradable
raise an exception (which will be apt.package.NotUpgradableError)




### Schedule:





Implement as soon as possible.



