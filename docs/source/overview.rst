.. _overview:

========
Overview
========

.. contents::
    :local:
    :depth: 2

.. todo:: The Birdhouse Overview needs to be updated.

What is WPS?
============

**Geographic Information Processing for the Web**
    *The Web Processing Service (WPS) offers a simple web-based method of finding, accessing, and using all kinds of calculations and models*.

.. note:: Read the documenation on `Geographic Information Processing for the Web <http://geoprocessing.info/wpsdoc/>`_

.. _wps_use_case:

WPS Use Case
============

A user runs WPS processes *remotely* on a machine with direct access to climate data archives.

.. image:: _images/wps_adamsteer.png

.. _birdhouse_overview:

Birdhouse Architecture
======================

.. image:: _images/birdhouse-components.png

ESGF_ is currently the main climate data resource (but more resources are possible).
ESGF Solr-index is used to find ESGF data.
The ESGF identity provider with OpenIDs and X509 certificate is used for authentication.

There are several WPS services. Malleefowl_ is the main one for the Phoenix_ client.
Malleefowl is used to search, download (with caching) ESGF data and to retrieve certificates.
Malleefowl has also a workflow engine (dispel4py_) to chain WPS processes.

The results of the WPS processes are stored on the file system and are accessible via URL (with a token id).

Results can be shown on a Map using a Web Mapping Service (ncWMS, adagucserver).

The PyCSW Catalog Service is used to register WPS services and also to publish WPS outputs.
Published results in the PyCSW can also used as input source for processes again.

WPS serivces can be accessed through web-applications like Phoenix or from scripts.

.. note:: See also the `Birdhouse Presentation`_.

.. _Birdhouse Presentation: https://github.com/bird-house/birdhouse-presentation
