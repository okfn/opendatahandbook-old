============
File Formats
============

An Overview of File Formats
===========================

JSON
----

JSON  is a very simple file format that is very easy for any programming language to read. Its simplicity means that is generally easier for computers to process than others, such as XML.

XML
---

XML is a widely used format for data exchange because it gives good opportunities to keep the structure in the data and the way files is built on, lets developers write parts of the documentation in with the data without interfering with the reading of them.

RDF
---

A relatively new format called RDF makes it possible to present data in a form that machinery can partially understand and interpret data. This format is used partly by the British Government Linked Open Data project. RDF is still not as widespread yet and there is limited tool support obligations for it, but it offers excellent opportunities for automatic data processing.

Spreadsheets
------------

Many authorities have information left in the spreadsheet, for example Microsoft Excel. This data can often be used immediately with the correct descriptions of what the different columns mean.

However, in some cases be macros and formulas in spreadsheets, which may be somewhat more cumbersome to have to do. It is therefore advisable to document such calculations next to the spreadsheet, since it is generally more accessible for users to read.

Comma Separated Files
---------------------

CSV files can be a very useful format because it is compact and thus suitable to transfer large sets of data with the same structure. However, the format is so spartan that data are often useless without documentation since it can be almost impossible to guess the significance of the different columns. It is therefore particularly important for the comma-separated formats that documentation of the individual fields are accurate.

Furthermore it is essential that the structure of the file are respected, as a single omission of a field may disturb the reading of all remaining data in the file without any real opportunity to rectify it, because it could not determine how the remaining data must be interpreted .

Text Document
-------------

Classic documents in formats like Word, ODF, OOXML, or PDF may be sufficient to show certain kinds of data - for example, relatively stable mailing lists or equivalent. It may be cheap to exhibit in, as often is the format data is born in. The format gives no support to keep the structure consistent, which often means that it is difficult to enter data by automated means. Be sure to use templates as the basis of documents that will display data for reuse, so it requires at least possible to pull information out of documents.

It can also support the further use of data to use typography markup as much as possible so that it becomes easier for a machine to distinguish headings (any type specified) from the content and so on. Generally it is recommended not to exhibit in word processing format, if data exists in a different format.

Plain Text
----------

Plain text documents (.txt) are very easy for computers to read, They generally exclude structural metadata from inside the document however, meaning that developers will need to create a parser that can interpret each document as it appears.

Some problems can be caused by switching plain text files between operating systems. MS Windows, Mac OS X and other Unix variants have their own way of telling the computer that they have reached the end of the line.

Scanned image
-------------

Probably the least suitable form for most data, but both TIFF and JPEG-2000 can at least mark them with documentation of what is in the picture - right up to mark up an image of a document with full text content of the document. It may be relevant to their displaying data as images whose data are not born electronically - an obvious example is the old church records and other archival material - and a picture is better than nothing.

Proprietary formats
-------------------

Some dedicated systems, etc. have their own data formats that they can save or export data in.
It can sometimes be enough to expose data in such a format - especially if it is expected that further use would be in a similar system as that they come from.It should always be indicated, where you can find more information on these proprietary formats, for example by providing a link to the supplier's website. Generally it is recommended to display data in a non-proprietary formats, where feasible.

HTML
----

Although many data are now available in HTML format at various sites. This may well be sufficient since the data are very stable and limited in scope. In some cases, it could be preferable to have data in a form more easily download and manipulate, but as it is cheap and easy to refer to a page on a website, it might be a good starting point in the display of data .

Typically it would be most appropriate to use tables in HTML documents to hold data, and here it is important that the various data fields are displayed, are given IDs which make it easy to find and manipulate data. Yahoo has developed a tool (http://developer.yahoo.com/yql/) that can extract structured information from a website, and such tools can do much more with the data if they are carefully tagged.


Open File Formats
=================

Even if information is provided in electronic, machine-readable format, and in detail, there may be issues relating to the format of the file itself.

The formats in which information is published – in other words, the digital base in which the information is stored - can either be “open” or “closed”. An open format is one where the specifications for the software are available to anyone, free of charge, so that anyone can use these specifications in their own software without any limitations on reuse imposed by intellectual property rights.

If a file format is “closed”, this may be either because the file format is proprietary and the specification is not publicly available, or because the file format is proprietary and even though the specification has been made public, reuse is limited. If information is released in a closed file format, this can cause significant obstacles to reusing the information encoded in it, forcing those who wish to use the information to buy the necessary software.

The benefit of open file formats is that they permit developers to produce multiple software packages and services using these formats. This then minimises the obstacles to reusing the information they contain.

Using proprietary file formats for which the specification is not publicly available can create dependence on third-party software or file format license holders. In worst-case scenarios this can mean that information can only be read using certain software packages, which can be prohibitively expensive, or which may become obsolete.

The preference from the open government data perspective therefore is that information be released in **open file formats which are machine-readable.**

Example: UK traffic data
------------------------

Andrew Nicolson is a software developer who was involved in an (ultimately successful) campaign against the construction of a new road, the Westbury Eastern bypass, in the UK. Andrew was interested in accessing and using the road traffic data that was being used to justify the proposals. He managed to obtain some of the relevant data via freedom of information requests, but the local government provided the data in a proprietary format which can only be read using software produced by a company called Saturn, who specialise in traffic modelling and forecasting. There is no provision for a “read only” version of the software, so Andrew's group had no choice but to purchase a software license, eventually paying £500 (€600) when making use of an educational discount. The main software packages on the April 2010 price list from Saturn start at £13,000 (over €15,000), a price which is most likely beyond the reach of most ordinary citizens.2

Although no access to information law gives a right of access to information in open formats, open government data initiatives are starting to be accompanied by policy documents which stipulate that official information must be made available in open file formats. Setting the gold standard has been the Obama Administration, with the Open Government Directive issued in December 2009, which says that:

To the extent practicable and subject to valid restrictions, agencies should publish information online in an open format that can be retrieved, downloaded, indexed, and searched by commonly used web search applications. An open format is one that is platform independent, machine readable, and made available to the public without restrictions that would impede the re-use of that information.3


How do I use a given format?
============================

When Authority must exhibit new data - that data has not been exhibited before - you should choose the format that provides the best balance between cost and suitability for purpose. For each format there are some things you should be aware of, and this section aims to affect them.

This section focuses only on how the cut surfaces are best arranged so that machines can access them directly. Advice and guidance about how web sites and web solutions should be designed, you can find elsewhere.

Web services
------------

For data that change frequently, and where each pull is limited in size, it is very relevant to expose data through web services. There are several ways to create a web service, but some of the most used is SOAP and REST. Generally, SOAP over REST, REST services, but are very easy to develop and use, so it is a widely used standard.

Database
--------

Like Web services provide direct database access to access data dynamically. Databases have the advantage that they can allow users to put together just the extraction, they are interested in.

There are some security concerns by allowing remote database extraction and database access is only useful if the structure of the database and the importance of individual tables and fields are well documented. Often, relatively simply and inexpensively create Web services that exposes data from a database, which can be an easy way to address safety concerns.


