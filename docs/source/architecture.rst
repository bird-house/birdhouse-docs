.. _birdhouse_overview:


Architecture
============

.. contents::
    :local:
    :depth: 2


Framework Overview
------------------

.. image:: _images/framework.png

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

Birdhouse is the home of Web Processing Services used in climate science and
components to support them (the birds):


.. _client_components:

Client Side Components
----------------------

* `Phoenix`_: a web-based WPS client with ESGF data access
* `Birdy`_: a WPS command line client and native library

.. _server_components:

Server Side Components
----------------------

WPS services for climate data analysis:

* `Emu`_: some example WPS processes for demo
* `Flyingpigeon`_: Testbed for new process development
* `Black Swan`_: services for the extreme weather event assessments
* `Hummingbird`_: provides cdo and compliance-checker as a service
* Finch: services for climate indices calculation
* Kingfisher: Services for Earth-Observation data analysis 

Many climate analysis operations are implemented using OpenClimateGIS_
including the `python package icclim <http://icclim.readthedocs.io/en/latest/>`_.

Supporting Services and libraries:

* `Twitcher`_: an OWS Security Proxy
* `Malleefowl`_: access to climate data (ESGF, ...) as a service
* `Eggshell`_: provides common functionallity for Birdhouse WPS services

You can find the source code of all birdhouse components on GitHub_.
Docker images with birdhouse components are on `Docker Hub`_

.. _GitHub: https://github.com/bird-house
.. _`Docker Hub`: https://hub.docker.com/r/birdhouse
