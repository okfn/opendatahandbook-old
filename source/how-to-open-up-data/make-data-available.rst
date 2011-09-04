========================================
Make Data Available (Technical Openness)
========================================


:term:`Open data` needs to be technically open as well as legally open. 
Specifically, the data needs to be available in bulk in a :term:`machine-readable` 
format.

Available
  Data should be priced at no more than a reasonable cost of reproduction, 
  preferably as a free download from the Internet. This pricing model is
  achieved because your agency should not undertake any cost when it
  provides data for use. 

In bulk
  The data should be available as a complete set. If you have a register
  which is collected under statue, the entire register should be available
  for download. A web API or similar service may also be very useful, but 
  they are not a substitutes for bulk access.

In an open, machine-readable format
  Re-use of data held by the public sector should not be subject to patent
  restrictions. More importantly, making sure that you are providing 
  machine-readable formats allows for greatest re-use. To illustrate this,
  consider statistics published as :abbr:`PDF (Portable Document 
  Format)` 
  documents, often used for high quality printing. While these statistics
  can be read by humans, they are very hard for a computer to use. This
  greatly limits the ability for others to reuse that data.

Here are a few policies that will be of great benefit:

* keep it simple, 
* move fast, and 
* be pragmatic

In particular it is better to give out raw data now than perfect data in 
six months' time.

There are many different ways to make data available to others. The most 
natural in the Internet age being online publication. There are many
variations to this model. At its most basic, agencies make their data 
available via their websites and a central catalogue directs visitors
to the appropriate source.  However, there are alternatives.

When :term:`connectivity` is limited or the size of the data are extremely 
large, distribution via other formats, can be warranted. This section will 
also discuss alternatives, which can act to keep prices very low.

Online methods
==============

via your existing website
-------------------------

The system which will be most familiar to your web content teams is to
provide files for download from webpages. Just as you currently 
provide access to discussion documents, data files are perfectly happy
to be made available this way.

One difficulty with this approach is that it is very difficult for an
outsider to discover where to find updated information. This option
places quite a bit of burden on the people creating tools with your
data.

via 3rd party sites
--------------------

Many repositories have become hubs of data in particular fields.
For example, pachube.com is designed to connect people with sensors to
those who wish to access data from them. Sites like Infochimps.com and 
Talis.com allow public sector agencies to store massive quantities of
data for free.

Third party sites can be very useful. The main reason for this is that
they have already pooled together a community of interested people and
other sets of data. When your data is part of these platforms, a a 
type of positive compound interest is created. 

Wholesale data platforms already provide the infrastructure which can 
support the demand. They often provide analytics and usage information. 
For public sector agencies, they are generally free.

These platforms can have two costs. The first is independence. Your 
agency needs to be able to yield control to others. This is often 
politically, legally or operationally difficult. The second cost may 
be openness. Ensure that your data platform is agnostic of who can 
access it. Software developers and scientists use many operating sytems,
from smart phones to supercomputers. They should all be able to access
the data.


via FTP servers
---------------

A less fashionable method for providing access to files is via the
File Transfer Protocol (FTP). This may be suitable if your audience is 
technical, such as software developers and scientists. The FTP system
works in place of HTTP, but is specifically designed to support file
transfers.

FTP has fallen out of favour. Rather than providing a website, looking
through an FTP server is much like looking through folders on a 
computer. Therefore, even though it is fit for purpose, there is far
less capacity for web development firms to charge for customisation.

as torrents
-----------

:term:`BitTorrent` is a system which has become familiar to policy makers 
because of its association with copyright infringement. BitTorrent uses
files called torrents, which work by splitting the cost of distributing 
files between all of the people accessing those files. Instead of servers
becoming overloaded, as the demand increases, so does the supply. This is
the reason that this system is so successful for  sharing movies. It is a 
wonderfully efficient way to distribute very large volumes of data.

as an API
---------

Data can be published via an :term:`Application Programming Interface` (API). 
These interfaces have become very popular. They allow programmers to
select specific portions of the data at a time, rather than providing
all of the data in bulk as a large file. APIs are typically connected
to a database which is being updated in real-time. This means that 
making information available via an API can ensure that it is up to 
date.

Publishing raw data in bulk should be the primary concern of all open
data intiatives. There are a number of costs to providing an API:

1. The price. They require much more development and maintainence 
   than providing files.
2. The expectations. In order to foster a community of users 
   behind the system, it is important to provide certainty. When things
   go wrong, you will be expected to incur the costs of fixing them.

Access to bulk data ensures that: 

a) there is no dependency on the original provider of the data, meaning
   if a restructure or budget cycle changes the situation, the data are
   still available.
b) anyone else can obtain a copy and redistribute it. This reduces the
   cost of distribution away from the source agency and means that there
   is no single point of failure.
c) others can develop their own services using the data, because they
   have certainty that the data will not be taken away from them.

Providing data in bulk allows others to use the data beyond its original
purposes. For example, it allows converting it into a new format, linking 
with other resources, data to be versioned and archived in multiple 
places. While the latest version of the data may be made available via 
an API, raw data should be made available in bulk at regular intervals.

For example, the Eurostat statistical service has a bulk download 
facility offering over 4000 data files. It is updated twice a day, offers 
data in :term:`Tab-separated values` (TSV) format, and includes 
documentation about the download facility as well as about the data files.

Another example is the District of Columbia OCTO’s Data Catalogue, which 
allows data to be downloaded in CSV and XLS format, in addition to live 
feeds of the data.

via the data access protocol
----------------------------

:term:`DAP` (Data Access Protocol) is a system for data transfer that was
developed for use in meterology and climate science. The system was 
designed to enable third-parties to access sections of databases stored
in some central location. Despite its origins in a particular field, the 
technology is very generic and can be adapted for data transfer in any 
area.

Implementing this technology can enable your agency to be experimental 
with its knowledge. For example, Australia's `Bureau of Meteorology Research Centre`_ 
provides the following disclaimer on its material:

    Please note that the following products ... do not currently form
    part of the Bureau's standard services in any way.

This example demonstrates that it is possible to provide data in raw form 
without incurring liability for others' use of that data.

 .. _Bureau of Meteorology Research Centre: http://opendap.bom.gov.au/index.shtml

via WebDAV
----------

`WebDAV`_, or Web-based Distributed Authoring and Versioning, is an attempt at
making the internet a read/write medium. It is a widely supported open standard
that supports locking and distributed authorship. 

Providing a service such as this could be useful for situations
where your agency would like to handle receiving improvements to data that 
it stores. The agency could provide its original data as the orginal source
and then refer to higher-quality, but unverified derivative data source for 
users with different needs.

  .. _WebDAV: http://en.wikipedia.org/wiki/WebDAV

Offline methods
===============

via optical media
-----------------

Optical media, such as DVDs, are very cheap to produce. However, they 
tend to lack the capacity that would warrant the manual handling of 
distributing them. One exception to this is events. If you are hosting 
an event for developers, such as a hackfest or barcamp, optical media 
can be the best way to distribute a dataset for use in the venue.


via external hard disk drives
-----------------------------

Hard disk drives can be very useful for data transfers in the terabyte
range. To support this, you need to have some form of ability to 
receive funds to cover the purchase, handling and shipping of your data.

Be careful to make sure that you are not charging for the data. Instead,
your fee should be as close to the actual cost of distribution as 
possible.
