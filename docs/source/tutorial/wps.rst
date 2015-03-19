.. _wps_tutorial:

What is WPS?
============

The Web Processing Service (WPS) offers a simple web-based method of finding, accessing, and using all kinds of calculations and models.

http://geoprocessing.info/wpsdoc/Concepts#what


Offering your functions as simple web service. The service is self-describing. can be called sync and async. 

.. contents::
    :local:
    :depth: 2

Defining a function
-------------------

Having this function::

    def summer_days(files, from_date, to_date, region=None):
        """Calculates number of summer days.
        """
        num_days = 0
        plot = None
        return num_days, plot

Parts of the function:

* identifier: summer_days
* description: Calculates number of summer days
* input parameters:
* output parameters: num_days (integer)

WPS definition
--------------

* defining inputs and outputs

Chaining WPS
------------

http://geoprocessing.info/wpsdoc/Concepts#chaining

* call them manually
* chain with wps ... output becomes input of another process
* chaining with workflow ... max. flexiblity

WPS definition with PyWPS
-------------------------

Using WPS
---------

http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2:_Introduction_to_WPS

* getcaps
http://geoprocessing.info/wpsdoc/1x0GetCapabilities
* describe
http://geoprocessing.info/wpsdoc/1x0DescribeProcess
* execute
http://geoprocessing.info/wpsdoc/1x0ExecuteGET


Calling with Birdy
------------------

Showing on a Map
----------------

using ipython notebook ...


WPS Documentation
-----------------

* `What is WPS? <http://geoprocessing.info/wpsdoc/Concepts#what>`_
* `WPS tutorial <http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2:_Introduction_to_WPS>`_
* `OGC Web Processing Service Standard <http://www.opengeospatial.org/standards/wps>`_

