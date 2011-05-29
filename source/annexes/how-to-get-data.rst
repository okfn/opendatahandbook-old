===============
How to get data
===============

This guide focuses on how you can extract data from web sites and 
web services. We will go over the various resources at your disposal
to find sources which are useful to you.


Directories
-----------

**Search Engines**

There are a small number of emerging search engines for raw data:

 * `opendatasearch.org`_ is a search engine which collects linked data from
   various directories.
 * The `Open Data Directory` provides wide coverage of many catalogues.
   At this stage, the directory's metadata is released under a 
   non-commercial licence.
 
**Edited directories**

One of the `largest directories of open data repositories`_ is provided 
by the `Open Access Directory`_. Its collection is mostly focused on 
scientific or research data and is curated by topic area. Topics covered 
the directory include archaeology, astronomy, biology, chemistry, 
computer science, energy, environmental sciences, earth sciences,
linguistics, marine sciences, medicine, physics and social sciences.

`CKAN`_ is a directory that largely works through wiki-like edits. Some 
of the benefits of CKAN are that it has well developed client libraries 
that enable you to programmatically access information about each of the 
datasets within its directory. For example, it is easy to ask it to 
tell you which datasets have been released into the public domain.

`Quora`_ has actually become a great source of information about where 
to find data on specific topic areas. It has several questions related 
to this topic which are being continually updated. Some examples include:

* `What are some free, public data sets? <http://www.quora.com/Data/What-are-some-free-public-data-sets>`
*  `Where can I get large datasets open to the public <http://www.quora.com/Data/Where-can-I-get-large-datasets-open-to-the-public>`

  .. opendatasearch.org: http://www.opendatasearch.org/
  .. largest directories of open data repositories: http://oad.simmons.edu/oadwiki/Data_repositories
  .. Open Access Directory: http://oad.simmons.edu/oadwiki/About_OAD
  .. CKAN: http://ckan.net
  .. Quora: http://www.quora.com

Scraping
--------

Remember, the website is the API. If a site provides information full
information on its pages, but only offers you a limited access via its
search page.

**Structure of a scraper**

Scrapers are comprised of three core parts:

1) A queue of pages to scrape
2) An area for structured data to be stored, such as a database
3) A downloader and parser that adds URLs to the queue and/or
   structured information to the database.

**Useful clean up steps**

One advantage of scraping data from the web is that you can actually 
have a better dataset than the original. Because you need to take steps
to understand the dataset's inconsistencies, you can eliminate or at least
minimise them. From another perspective, spending time cleaning up 
messy data can fill the large gaps that your processor will experience
when waiting for it to be downloaded from its host.

This section provides an example of several useful clean-up operations.

* Strip whitespace
* Convert data to integers or Boolean values: `'Yes' -> True`

Converting yes/no to Boolean values

Computers are far better at interpreting Boolean values when they are 
consistently provided. Irrespective of the programming language, normalising
these values will make any automatic comparisions much richer.

    def


Converting numbers to the correct type

If you're extracting number from HTML tables, they will each be 
represented as a `string` or Unicode, even though it would be 
more sensible to treat as integers or floating point numbers:: 

    def to_int(number, european=False):
        """ 
        >>> to_int('32')
        32
        >>> to_int('3,998')
        3998
        >>> to_int('3.998', european=True)
        3998
        """
        if european:
            number = number.replace('.', '')
        else:
            number = number.replace(',', '')
        return int(number)

    def to_float(number, european=False)
        """
        >>> to_float(u'42.1')
        42.1
        >>> to_float(u'32,1', european=True)
        32.1
        >>> to_float('3,132.87')
        3132.87
        >>> to_float('3.132,87')
        3132.87
        >>> to_float('(54.12)')
        -54.12

        Warning
        -------

        Incorrectly declaring `european` leads to troublesome results:

        >>> to_float('54.2', european=True)
        542
        """
        import string
        if european:
            table = string.maketrans(',.','.,')
            number = string.translate(number, table)
        number = number.replace(',', '')
        if number.startswith('(') and number.endswith(')'):
            number = '-' + number[1:-1] 
        return float(number)

If you are dealing with numbers from another region consistently, it may be
appropriate to call upon the `locale` module. You will then have the advantage
of code written in C, rather than Python::

    >>> import locale
    >>> locale.setlocale(locale.LC_ALL, '')
    >>> locale.atoi('1,000,000')
    1000000

Stripping whitespace

Removing whitespace from a string is built into many languages
`string`. Removing left and right whitespace is highly 
recommended. Your database will be unable to sort data properly
which have inconsistent treatment of whitespace:: 

    >>> u'\n\tTitle'.strip()
    u'Title'

Converting dates to a machine-readable format.

Python is well blessed with a `mature date parser`_, `dateutil`. 
We can take advantage of this to make light work an otherwise
error-prone task.

`dateutil` can be reluctant to raise exceptions to dates that 
it doesn't understand. Therefore, it can be wise to store the 
original along with the parsed ISO formatted string. This can 
be used for manual checking if required later.

Example code::

    def date_to_iso(datestring):
        """
        Takes a string of a human-readable date and
        returns a machine-readable date string.


        >>> date_to_iso('20 July 2002')
        '2002-07-20 00:00:00'
        >>> date_to_iso('June 3 2009 at 4am')
        '2009-06-03 04:00:00'
        """
        from dateutil import parser
        from datetime import datetime
        default = datetime(year=1, month=1, day=1)
        return str(parser.parse(datestring, default=default))
  
  .. mature date parser: http://www.labix.org/python-dateutil

**General tips**

Minimising the pages to scrape. This will save everybody time and 
resources.


* Inspect any AJAX fields. AJAX is generally performed by sending 
  JavaScript objects between the server and the web browser. They
  are easy to parse and are generally very rich.
* Try looking for a `sitemap.xml`.
* Any pages in the `robots.txt` which disallow access are generally 
  where the bulk of the value lies.


**Types of scrapers**

The structure of most scrapers is generally 

XPath
  XPath uses the structure of the page and tag attributes to be able
  to select . XPath expressions can look fairly complex and take some
  a moderate degree of 

Template
  Regular expressions to look for common patterns in the text. One of 
  the easiest template extraction systems is `scrapemark`_. While it
  is not the most computationally efficient 

Machine-learning
  Machine-learning packages work by training a model of example pages,
  then asking for matching material.

**Infrastructure**

It's possible to use sophisticated techniques to circumvent rate limitations
and IP address blocking. The best technique for achieving this though is by
being a good netizen and adding pauses between your requests.

When generating open data however, you should use ScraperWiki. ScraperWiki
allows people to cooperatively build scrapers. They will also take care of 
rerunning your scraper periodicly so that new data are added.




  .. scrapemark: https://github.com/arshaw/scrapemark

============================================
How to build your city's open data catalogue
============================================

Max Ogden has a great post about the practical steps needed to build 
an open data API for a city.
