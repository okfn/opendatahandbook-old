Mercurial repository for the `Open Data Manual`_.

.. _Open Data Manual: http://opendatamanual.org/

Authoratative source is on bitbucket: https://bitbucket.org/okfn/opendatamanual

The source in this repository was pulled from the markdown that is live on the
`Open Data Manual`_ site. We are in the process of transitioning to full
restructured text and using `Sphinx`_ to generate HTML (that can then be uploaded
to wordpress or elsewhere).

.. _Sphinx: http://sphinx.pocoo.org/


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
 
