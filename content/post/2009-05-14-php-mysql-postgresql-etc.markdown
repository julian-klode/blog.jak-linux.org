---
author: juliank
date: 2009-05-14 16:02:45+00:00
draft: false
title: PHP, MySQL, PostgreSQL, etc.
type: post
url: /2009/05/14/php-mysql-postgresql-etc/
categories:
- General
---

Well, I'm currently writing a PHP and SQL application at school, so here are some of my thoughts on the problems I encounter.


## PHP is crap


Many PHP applications are low quality applications. The problem is that PHP makes it hard for developers to write good applications. PHP developers tend to use many global variables, global code, and not many classes or functions. And when writing applications for the web, PHP makes it easy to mix PHP and HTML, in my opinion even too easy.

Well-written applications follow some basic rules. First, separate your code into functions and classes, and (2) split your code over multiple files. And there is one rule which is especially important for non-commandline applications: (3) seperate logic and presentation. This means if you write a web application, use a template engine.

PHP error and exception handling is also an interesting topic. The problem here lies in the distinction between the both. In my opinion, there should only be one way to handle such stuff: Using exceptions. Exceptions are a very widespread way to program today, and are used in languages like Java and Python for cases where PHP uses errors. The concept of PHP's errors results in code like `@do_something or die("blah"); ` being written in libraries which is a problem as it clearly violates rule (3) I wrote above, because there is no way to catch this die() error.

Furthemore, PHP has no clear concept of namespaces in the current stable versions (< 5.3). PHP 5.3 finally gets namespaces, but using a backslash character, which looks really bad and makes everyone think of eithers Windows systems or escape characters.

There are even more problems with PHP. From time to time, PHP just crashes with a segmentation fault.


## MySQL vs. PostgreSQL


MySQL seems to have many problems with checking data, which can confuse me. It got better in MySQL 5 with the introduction of the new sql_modes like STRICT_ALL_TABLES and TRADITIONAL. And using storage engines like InnoDB also allows you to take advantage of stuff like foreign keys and transactions. But MySQL is still problematic.

For example, in an application I wrote I had multiple entries identified by a numeric id (an INTEGER). One day, I wanted to check whether my error handling was OK and requested an entry with the invalid ID '1X', which resulted in `SELECT * from A where id='1X';`. Now I expected to get an error or at least no result, but MySQL happily proceeded with the query and returned the entry with the ID 1. I tried the same thing on PostgreSQL and got an error message that '1X' is not integer, as I expected it.

As another example, when I run the same PHP application using PDO on a MySQL database and a PostgreSQL database, I always get strings from the MySQL database whereas I get integers from PostgreSQL if the columns are integers.

Another thing which PostgreSQL does better than MySQL is password encryption. MySQL only provides access to the standard crypt() function and by default only generates DES passwords. It allows other methods to be used (although not all are available everywhere and therefore not documented), but it provides no way to create a salt for them, which makes them not very useful. PostgreSQL in contrast provides less encryption methods but it provides the gen_salt() function which can be used to generate salts for blowfish encryption (`gen_salt('bf')`).

Another problem is that MySQL simply ignores references when they are added to the column definition instead of a separate 'FOREIGN KEY'. Because MySQL gives no errors when a feature like REFERENCES is not supported, developers may think that the feature is supported and write code using this feature just to realize later that what they wrote does not what they want.

And you can't write AGPL applications using MySQL client libraries, because MySQL is GPL-2 which is incompatible with the AGPL. You might think that the "[FOSS License Exception](http://www.mysql.com/about/legal/licensing/foss-exception/)" helps here, but this only lists (among others) the GPL-3. Or am I wrong?

But PostgreSQL has other problems, at least when it comes to the performance of the information_schema.columns view. This may be related to the fact that PostgreSQL has > 1000 rows whereas MySQL only has 250. And PostgreSQL may be a bit harder to configure.


## Final words


All in all, PHP and MySQL are not the best choices for writing applications. They are to tolerant, and do not treat errors in an acceptable way -- by aborting the current action. I can get around some problems in PHP by using error handlers which raise exceptions and setting error_reporting to E_ALL, but in fact this should be the default. MySQL problems can be solved to a large extend by setting sql_mode to TRADTIONAL and using InnoDB databases, which should in my opinion be the default and not an option.

My recommendation is to use PostgreSQL servers and for the applications: use frameworks (if you are allowed to, which may not be always the case [e.g. when you are learning SQL, using a ORM is clearly the wrong way]), document your code, separate your code into classes and functions, and make sure you are not using to many global variables. And use a SCM to track your changes.
