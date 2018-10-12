---
author: juliank
date: 2009-02-12 17:42:19+00:00
draft: false
title: 'debimg core: creating a repository'
type: post
url: /2009/02/12/debimg-core-creating-a-repository/
categories:
- Debian
- debimg
---

As I wrote Monday in "debimg core example", I have an extended version which creates a repository. The problem on Monday was that the code was not far enough to be published. Not much has changed yet, but I considered to create a temporary branch temp/repository to be able to show you the example, and to give you an impression of what the final API will look like (it's not complete yet, trust me).

Now I will present you the example. It is not much longer than the pool example I gave on monday, but it does much more - it creates a repository (and it has some commandline options). The concept of the Repository is very simple, too. We have two classes, Repository and Distribution, and a Repository object contains multiple Distribution objects, which are responsible for packages and related stuff.


    
    
    #!/usr/bin/python
    # Copyright (C) 2009 Julian Andres Klode.
    #
    # Released under the terms of the GNU General Publice License, version 3
    # or (at your option) any later version.
    #
    """Example to demonstrate the power of debimg's repository management.
    
    This example creates a directory example.debimg, with two subdirectories:
        - pool: This holds debimg's file pool (see debimg.core.files.Pool)
        - repo: This holds the created repository (debimg.core.repository)
    
    It creates a repository of all required packages, using your local apt sources.
    """
    from __future__ import with_statement
    import operator
    import optparse
    import sys
    
    from debimg.core.resolver import Resolver
    from debimg.core.files import Pool
    from debimg.core.repository import Distribution, Repository
    
    def main():
        """Called when the script is executed."""
        parser = optparse.OptionParser()
        parser.add_option('-u', '--user', help='Same as in GPG')
        parser.add_option('-c', '--contents', action="store_true",
                         help='Create Contents-*.gz files')
        opts, args = parser.parse_args()
    
        # Create a pool, which manages the access to the files.
        pool = Pool('example.debimg/pool')
    
        # Create a resolver using your local apt configuration.
        pkgs = Resolver()
    
        # Create a new repository
        repo = Repository(pool, 'example.debimg/repo')
    
        # Create a new distribution and store it in dist.
        dist = repo.add_distribution('lenny')
    
        # Add all packages with priority required to the resolver
        pkgs.add_priority('required')
    
        # Add the packages from the resolver to the distribution
        for group in pkgs.groups():
            for package in group:
                dist.add_package(package)
    
        pool.compact()   # Optional step
        pool.fetch()     # Fetch all the packages from the mirror
        dist.finalize_files() # Link the files into the repository
        dist.finalize_packages() # Create Packages files (uncompressed and gzip)
    
        ##
        # If we want to create Contents-*.gz files, we can do this as well:
        # but we don't want to
        if opts.contents:
            dist.finalize_contents()
    
        # Now create our Release files, and sign them using the key provided on
        # the commandline. If no key has been provided, do not sign it.
        dist.finalize_release(Suite='testing', key=opts.user)
    
        for file in sorted(pool._files, key=operator.attrgetter('uri')):
            print file   # Print information about every file, sorted by URI.
    
    if __name__ == '__main__':
        main()
    



To try the code, checkout the temp/repository branch at git://git.debian.org/users/jak/debimg.git and execute the script named test-repository, which is the same as printed above. If you have questions, please ask. Also read the docstring of debimg.core.repository to see which changes are not yet done (eg. common base class for Distribution and Repository, and of course adding files manually).
