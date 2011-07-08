`Open Data Manual`_
===================

Introduction
------------

Welcome to the the `Open Data Manual`. We look forward to your contributions,
whether that's translation, feedback, editing or adding more content. The 
manual is a project of the `Open Knowledge Foundation`_. Its authoratative 
source is on bitbucket:

  <https://bitbucket.org/okfn/opendatamanual>


Roadmap
-------

The contributors plan on creating several Annexes to this manual. Each one
will cover different parts of the process surrounding open data.

Some of the things that we would like to include are:

+ Sources of open data
+ Cleaning data
+ Publishing data
+ Participating in the open data community


About these files
=================

The manual is written the `ReStructured Text`_ format. `ReStructured Text` allows
us to write files in plain text files, which can be nicely rendered as a website
or a PDF using `Sphinx`_.

However, we are currently in a transition process. The current `Open Data Manual`_ 
site uses Markdown. This means that the current source files are slightly
inconsistent and will not render properly.

Layout of this Repository
=========================

Layout of the repository::

  # the manual
  source/
  # useful scripts
  bin/
  # output 'built' html
  build/

Building the Documentation
==========================

1. Install `Sphinx` >= 0.6 (Debian/Ubuntu: apt-get install python-sphinx)
2. Run the build using the Makefile::

    make html
    

Helping with the project
========================

Areas of help needed:

+ Content writing
+ Editing
+ Translation

Tools you will need
-------------------

In order to contribute, there are a few required tools. At a minimum, you
need a text editor. However, there are some other tools which will aid you
significantly. These are:

+ Mercurial, our version control tool
+ Sphinx, the tool that builds websites from these source files. 
+ XChat, a programme that allows you to communicate with the rest of the 
  OKFN in real time. 

To download these tools on Ubuntu, run::

    $ sudo apt-get install mercurial python-sphinx xchat

To download the manual, follow these commands::

    $ cd ~
    $ mkdir OKFN
    $ cd OKFN
    $ hg clone https://bitbucket.org/okfn/opendatamanual



.. _Open Data Manual: http://opendatamanual.org/
.. _Open Knowledge Foundation: http://okfn.org/
.. _Sphinx: http://sphinx.pocoo.org/
 
