.. _wps_tutorial:

What is WPS?
============

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

Chaining WPS
------------

WPS definition with PyWPS
-------------------------

Using WPS
---------

* getcaps
* describe
* execute

Calling with Birdy
------------------

Showing on a Map
----------------

using ipython notebook ...


WPS Documentation
-----------------

* `What is WPS? <http://geoprocessing.info/wpsdoc/Concepts#what>`_
* `WPS tutorial <http://wiki.ieee-earth.org/Documents/GEOSS_Tutorials/GEOSS_Provider_Tutorials/Web_Processing_Service_Tutorial_for_GEOSS_Providers/Section_2:_Introduction_to_WPS>`_
* `Web Processing Service Information Site <http://geoprocessing.info/wpsdoc/index>`_
* `OGC Web Processing Service Standard <http://www.opengeospatial.org/standards/wps>`_

