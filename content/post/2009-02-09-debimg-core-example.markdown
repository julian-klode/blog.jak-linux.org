---
author: juliank
date: 2009-02-09 17:03:07+00:00
draft: false
title: debimg core example
type: post
url: /2009/02/09/debimg-core-example/
categories:
- Debian
- debimg
---

The following example demonstrates the features of debimg core, and how it can be used to fetch a some packages. As you will see when you run this example, debimg uses SHA1 filenames for the downloaded files. This may be changed in a future version.

There is also an improved version of this example, which creates a repository, but the needed module (debimg.core.repository) is not public yet, because its far from being finished. I expect to complete repository code on Wednesday.

    
    
    #!/usr/bin/python
    # Copyright (C) 2009 Julian Andres Klode.
    #
    # Released under the terms of the GNU General Publice License, version 3
    # or (at your option) any later version.
    #
    """Example to demonstrate the power of debimg's pool
    
    This example creates a directory example.debimg, with two subdirectories:
    - pool: This holds debimg's file pool (see debimg.core.files.Pool)
    """
    from debimg.core.resolver import Resolver
    from debimg.core.files import Pool
    
    def main():
        """Called when the script is executed."""
    
        # Create a pool, which manages the access to the files.
        pool = Pool('example.debimg/pool')
    
        # Create a resolver using your local apt configuration.
        pkgs = Resolver()
    
        # Add all packages with priority required to the resolver
        pkgs.add_priority('required')
    
        # Add the packages from the resolver to the pool
        for group in pkgs.groups():
            for package in group:
                pool.add_package(package)
    
        pool.fetch() # Fetch all the packages from the mirror
    
        for file in sorted(pool._files, key=lambda k: k.uri):
            print file # Print information about every file, sorted by URI.
    
    if __name__ == '__main__':
        main()
    
