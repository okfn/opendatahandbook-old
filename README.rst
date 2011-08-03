`Open Data Manual`_
===================

Introduction
------------

Welcome to the source for the `Open Data Manual`. The manual is a project of
the `Open Knowledge Foundation`_.  If you are reading this it is likely you are
looking to contribute in some way, whether that's translation, feedback,
editing or adding more content (if not and you just want to read the manual
please head over to the http://opendatamanual.org/).

.. _Open Data Manual: http://opendatamanual.org/
.. _Open Knowledge Foundation: http://okfn.org/
.. _Sphinx: http://sphinx.pocoo.org/

Contributing to the project
---------------------------

See http://wiki.okfn.org/Open_Data_Manual#Contributing

Wiki
----

Main wiki page is: http://wiki.okfn.org/Open_Data_Manual

This is also official 'home page' for development work on the manual.

Mailing List
------------

http://lists.okfn.org/mailman/listinfo/open-data-manual

Version Control
---------------

We manage the source using git and the official repository is here:

https://github.org/okfn/opendatamanual

Roadmap
-------

See the Manual's wiki page http://wiki.okfn.org/Open_Data_Manual and its issue
tracker: http://github.com/okfn/opendatamanual/issues


About these files
=================

The manual is written the `ReStructured Text`_ format. `ReStructured Text` allows
us to write files in plain text files, which can be nicely rendered as a website
or a PDF using `Sphinx`_.


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

1. Get the themes::

   git submodule init 
   git submodule update 

2. Install `Sphinx` >= 0.6 (Debian/Ubuntu: apt-get install python-sphinx)
3. Run the build using the Makefile::

    make html
    
Building for Translation (i18n)
-------------------------------

Generating pot files
~~~~~~~~~~~~~~~~~~~~

1. You will need to install sphinx HEAD (what will be v1.1). Do this from the
   official source repo: https://bitbucket.org/birkenfeld/sphinx/

2. Run::

    sphinx-build -b gettext source/ translation/pot

3. Resulting pot files will be in build/i18n

4. Add each pot files as a resource on
   https://www.transifex.net/projects/p/opendatamanual/ if not already there

Adding a new language
~~~~~~~~~~~~~~~~~~~~~

We use transifex for this.

1. Go to https://www.transifex.net/projects/p/opendatamanual/

2. For each resource add translation for specified language

