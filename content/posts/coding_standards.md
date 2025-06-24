---
title: "Post Title"
slug: post-title
created: 2024-12-31
updated: 2025-06-23
description: "A brief summary of what this page is about."
tags: [linux, self-hosting, minimalism]
draft: true
---


Here are my **personal** coding standards for some languages.

## Interpreted languages
#### Never put the file extension to the source file instead use a shebang.
`` 
    #!/bin/sh
    #!/bin/python3
    #!/bin/perl
``

## Posix shell
#### Always wrap variables with `"${}"` to prevent globbing.
`` 
    echo "${var}"
    echo "${1}"
    echo "${@}"
``

## Makefiles
#### If Makefile is fully posix complient and doesn't have anything extra add 
`.POSIX:` to the beginning of the file

## C 
#### Use K&R style `if`s
``
    if (condition) {
        do this;
        do that;
        do another;
    }
``
#### if only one line don't use curly braces.
``
    while (condition)
        do this
``

``
    if (condition)
        do this
    else
        do that
``
