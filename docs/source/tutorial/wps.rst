.. _wps_tutorial:

What is WPS?
============

The Web Processing Service (WPS) offers a simple web-based method of finding, accessing, and using all kinds of calculations and models.

http://geoprocessing.info/wpsdoc/Concepts#what


* Offering your functions as simple web service. 
* The service is self-describing. 
* can be called sync and async. 
* wps is just an interface description. several implementations can exist.
* is part of the :term:`OGC` standards family: :term:`wms`, wfc, wcs, sos, ...
* a lightweight specification. Comparable to :term:`xml-rpc` ... but xml-rpc is not self-describing.

.. contents::
    :local:
    :depth: 2

Defining a function
-------------------

Having this function::

    def count_words(file):
        """Calculates number of words in text document. 
        Returns JSON document with occurrences of each word.
        """
        return json_doc

Parts of the function:

* identifier: count_words
* description: Calculates number of words ...
* input parameters: file (mime type text/plain)
* output parameters: json_doc (mime type application/json)

WPS definition
--------------

To add a new proccess you just need to define the input and ouput parameters.

.. image:: ../_images/WpsInOut.png

Two types of parameters:

* Literal Parameters: integer, boolean, string, ...
* Complex Parameters: documents with mime-type (xml, cvs, jpg, netcdf, ...) as URL or directly

Parameters have:

* identifier: name of the parameter
* abstract: description of the parameter
* multiplicity: optional, one, many ... 
* allowed values: in case of literal parameters a list of allowed values.


Chaining WPS
------------

.. image:: ../_images/WpsChain.png

http://geoprocessing.info/wpsdoc/Concepts#chaining
http://geoserver.geo-solutions.it/edu/en/wps/chaining_processes.html

* call them manually
* chain with wps ... output becomes input of another process
* chaining with workflow ... max. flexibility

WPS definition with PyWPS
-------------------------

Implementation of word counter in PyWPS:

.. literalinclude:: wps_word_counter.py
    :language: python
    :emphasize-lines: 16,24,32
    :linenos:


Using WPS
---------

http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2:_Introduction_to_WPS

Operations:

* getcaps
http://geoprocessing.info/wpsdoc/1x0GetCapabilities

* describe
http://geoprocessing.info/wpsdoc/1x0DescribeProcess

* execute
http://geoprocessing.info/wpsdoc/1x0ExecuteGET


Calling with Birdy
------------------

Which proccess are available (`GetCapabilities`)::

  $ birdy -h
  usage: birdy [-h] <command> [<args>]

  optional arguments:
    -h, --help            show this help message and exit

  command:
    List of available commands (wps processes)

    {chomsky,helloworld,inout,ultimatequestionprocess,wordcount}
                        Run "birdy <command> -h" to get additional help.

What input and output parameters does `wordcount` have (`DescribeProcess`)::

  $ birdy wordcount -h
  usage: birdy wordcount [-h] --text [TEXT] [--output [{output} [{output} ...]]]

  optional arguments:
    -h, --help            show this help message and exit
    --text [TEXT]         Text document: URL of text document, mime
                        types=text/plain
    --output [{output} [{output} ...]]
                        Output: output=Word count result, mime
                        types=text/plain (default: all outputs)

Run `wordcount` with a text document (`Execute`)::

  $ birdy wordcount --text http://birdhouse.readthedocs.org/en/latest/index.html
  Execution status: ProcessAccepted
  Execution status: ProcessSucceeded
  Output:
  output=http://localhost:8090/wpsoutputs/emu/output-37445d08-cf0f-11e4-ab7e-68f72837e1b4.txt 

WPS Documentation
-----------------

* `What is WPS? <http://geoprocessing.info/wpsdoc/Concepts#what>`_
* `WPS tutorial <http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2:_Introduction_to_WPS>`_
* `OGC Web Processing Service Standard <http://www.opengeospatial.org/standards/wps>`_
* `GeoServer tutorial <http://geoserver.geo-solutions.it/edu/en/wps/index.html>`_

