###############
How to get data
###############

.. sectionauthor:: Tim McNamara <tim.mcnamara@okfn.org>

This guide focuses on how you can extract data from web sites and 
web services. We will go over the various resources at your disposal
to find sources which are useful to you.

************
Finding data
************

Directories
===========

Search Engines
--------------

There are a small number of emerging search engines for raw data:

 * `opendatasearch.org`_ is a search engine which collects linked data from
   various directories.
 * The `Open Data Directory` provides wide coverage of many catalogues.
   At this stage, the directory's metadata is released under a 
   non-commercial licence.
 
Edited directories
------------------

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

***************
Extracting Data
***************

.. 
   TODO
     OData
     REST APIs
      - ideas to get all results when there is no list given
      - paginating through all results as iterators
     Feeds - RSS/Atom

Scraping
========

Remember, the website is the API. If a site provides information full
information on its pages, but only offers you a limited access via its
search page.

Structure of a scraper
----------------------

Scrapers are comprised of three core parts:

1) A queue of pages to scrape
2) An area for structured data to be stored, such as a database
3) A downloader and parser that adds URLs to the queue and/or
   structured information to the database.

Useful clean up steps
---------------------

One advantage of scraping data from the web is that you can actually 
have a better dataset than the original. Because you need to take steps
to understand the dataset's inconsistencies, you can eliminate or at least
minimise them. From another perspective, spending time cleaning up 
messy data can fill the large gaps that your processor will experience
when waiting for it to be downloaded from its host.

This section provides an example of several useful clean-up operations.

* Cleaning HTML
* Strip whitespace
* Converting numbers to number types: 
* Converting Boolean values: `'Yes' -> True`
* Converting dates to machine-readable formats: `"24 June 2004" -> "2004-06-24"`

Clean the HTML
^^^^^^^^^^^^^^

HTML you find on the web can be atrocious. Here's a quick function that 
can help. We make use of the `lxml`_ library. It'svery good at 
understanding broken HTML and will render a perfectly-formed page for 
your extractor functions to

You may be concerned that this is computationally wasteful. This is 
true, but it can reduce lots of the irritation of extracting specific
information from messy HTML::

    def clean_page(html, pretty_print=False):
        """
        >>> junk = "some random HTML<P> for you to try to parse</p>"
        >>> clean_page(junk)
        '<div><p>some random HTML</p><p> for you to try to parse</p></div>'
        >>> print clean_page(junk, pretty_print=True)
        <div>
        <p>some random HTML</p>
        <p> for you to try to parse</p>
        </div>
        """
        from lxml.html import fromstring
        from lxml.html import tostring
        return tostring(fromstring(html), pretty_print=pretty_print)

Converting yes/no to Boolean values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Computers are far better at interpreting Boolean values when they are 
consistently provided. Irrespective of the programming language, normalising
these values will make any automatic comparisions much richer::

    def to_bool(yes_no, none_to_false=True):
        """
        >>> to_bool('')
        False
        >>> to_bool(None):
        False
        >>> to_bool('y')
        True
        >>> to_bool('yip')
        True
        >>> to_bool('Yes')
        True
        >>> to_bool('nuh')
        False
        """
        yes_no = yes_no.strip().lower()
        if not yes_no.strip() and none_to_false:
            return False
        if yes_no.startswith('y'):
            return True
        elif yes_no.startswith('n'):
            return False

Converting numbers to the correct type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^

Removing whitespace from a string is built into many languages
`string`. Removing left and right whitespace is highly 
recommended. Your database will be unable to sort data properly
which have inconsistent treatment of whitespace:: 

    >>> u'\n\tTitle'.strip()
    u'Title'

Converting dates to a machine-readable format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

General tips
------------

* Minimise the pages to scrape. This will save everybody time and 
  resources.

  * Inspect any AJAX fields. AJAX is generally performed by sending 
    JavaScript objects between the server and the web browser. They
    are easy to parse and are generally very rich.
  * Try looking for a `sitemap.xml`.
  * Any pages in the `robots.txt` which disallow access are generally 
    where the bulk of the value lies.

* Run an evented or multi-threaded system. Once you have gained the 
  confidence of building a few scrapers, learn how to optimise 
  performance. Given that you are using lots of external resources,
  there will be lots of latency involved. This means that your scraper's
  performance by using asynchronous programming.


Types of scrapers
-----------------

:DOM-based approaches:
  This is the most common form of scraper. All the data that you are
  looking to extract is identified by selecting portions from the DOM.

  Most modern libraries, such as `lxml`_ accept CSS selectors. So, in
  Python to extract the 

  XPath uses the structure of the page and tag attributes to be able
  to select . XPath expressions can look fairly complex and take some
  a moderate degree of 

  

:Template:
  Regular expressions to look for common patterns in the text. One of 
  the easiest template extraction systems is `scrapemark`_. While it
  is not the most computationally efficient 

:Machine-learning:
  Machine-learning packages work by training a model of example pages,
  then asking for matching material.

  .. lxml : http://lxml.de/

A scraping framework
--------------------

Let's demonstrate some of the principles that we have been talking about. 

We'll be creating a scraping framework, called `tbd`.

::
    """
    {{somthing}}.py : a webscraping framework..
    """
    import bsddb
    import pickle
    import urllib2
    from asynchat import fifo

    from dateutil import parser as date_parser
    import lxml
    import lxml.html

    START_URL = 'http://blog.okfn.org/'
    db = bsddb.hashopen('okfnblog.db')

    #
    # UTILITY FUNCTIONS
    #

    def get_clean_page(url):
        page = get_page(url)
        page = lxml.html.tostring(page)
        page = lxml.html.fromstring(page)
        return page

    def get_page(url):
        res = urllib2.urlopen(url)
        page = lxml.html.parse(res)
        page.make_links_absolute()
        return page

    def save_post(post):
        save(post['post_id'], post)

    def save_tag(tag):
        save('tag-%s' % tag['tag'], tag)

    def save_author(author):
        save('author-%s' % author['name'], author)

    def save(key, data):
        db[key] = pickle.dumps(data)

    def extract_created_at_datetime(post):
        date = post.cssselect('span.entry-date')[0].text
        time = post.cssselect('div.entry-meta a')[0].attrib['title']
        return str(date_parser.parse(date + ' ' + time))

    def process_post(url):
        source = get_page(url)
        post = {}
        post['title'] = source.cssselect('h1.entry-title')[0].text
        post['author'] = source.csselect('span.author a')[0].text
        post['content'] = source.cssselect('div.entry-content')[0].text_content()
        post['as_html'] = lxml.html.tostring(source.cssselect('div.entry-content')[0])
        post['created_at'] = extract_created_at_datetime(source)
        post['post_id'] = source.cssselect('div.post')[0].attrib['id']
        post['tags'] = [tag.text for tag in source.cssselect('a[rel~=tag]')]
        post['url'] = url
        yield save_post, post
        yield save_author, dict(name=post['author'])
        for tag in post['tags']
            yield save_tag, dict(tag=tag, post_id=post_id, author_name=post['author'])

    def process_archive(url):
        archive = get_page(url)
        for post in archive.cssselect('.post .entry-meta a'):
            yield process_post, post.attrib['href']
        previous = archive.cssselect('.nav-previous a')
        if previous: #is found
            yield process_archive, previous[0].attrib['href']

    def process_start(url):
        index = get_page(url)
        for anchor in index.cssselect('li#archives-2 a'):
            yield process_archive, anchor.attrib['href']
    
    def main():
        queue = fifo((process_start, START_URL))
        while 1:
            status, data = queue.pop()
            if status != 1:
                break
            func, args = data
            for newjob in func(args):
                queue.push(newjob[0], newjob[1])
            db.sync()
           




Infrastructure
--------------

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
