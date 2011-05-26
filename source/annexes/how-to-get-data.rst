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

More sophisticated scrapers will cache pages and will often add a 
post-download processing step.



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
