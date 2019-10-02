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

* Emu_: some example WPS processes for demo
* Flyingpigeon_: Testbed for new process development
* `Black Swan`_: services for the extreme weather event assessments
* Hummingbird_: provides cdo and compliance-checker as a service
* Finch_: services for climate indices calculation
* Kingfisher_: Services for Earth-Observation data analysis

Many climate analysis operations are implemented using OpenClimateGIS_
including the `python package icclim <http://icclim.readthedocs.io/en/latest/>`_.

Supporting Services and libraries:

* Twitcher_: an OWS Security Proxy
* Malleefowl_: access to climate data (ESGF, ...) as a service
* Eggshell_: provides common functionallity for Birdhouse WPS services

You can find the source code of all birdhouse components on GitHub_.
Docker images with birdhouse components are on `Docker Hub`_

Files and Folders
.................

.. _note: See also administrator guidelines

This is an overview of folder structure and important files for administration of a server-side birdhouse ecosystem.

It is recommended to clone the separated WPS services (birds) into one top level folder like:

.. code-block:: sh

  $ ~/birdhouse/emu
  $ ~/birdhouse/pyramid-pheonix
  $ ~/birdhouse/finch
  $ ~/birdhouse/malleefowl
  ...

The dependencies of each bird is deployed as `conda environment` and per default located at:

.. code-block:: sh

  $ ~/.conda/envs/

The environment of a bird is defined in `./{birdname}/environment.yml`.

Process descriptions are placed in `./{birdname}/{birdname}/processes/` while modules designed and used for the service
are situated in `./{birdname}/{birdname}/`. Here are also static data like shapefiles, templates or additional data used by the processes.

.. code-block:: sh

  $ ./{birdname}/{birdname}/data/shapefiles
  $ ./{birdname}/{birdname}/templates

Each birdhouse compartment has a documentation build with `Sphinx` and the corresponding files are situated in

.. code-block:: sh

  $ ./{birdname}/docs

When running a service, files and folders for input data, result storage, file cache of simply logfiles
are defined in the `./{birdname}/.config.cfg`. Default configuration is defined in `./{birdname}/{birdname}/default.cfg`
as well as an example can be found in `~./{birdname}/etc`.
For more options of configuration see the `pywps configuration instructions <https://pywps.readthedocs.io/en/master/configuration.html>`_

For development and deployment testing the installations be checked running tests (`make test`). Test descriptions testdata
are situated in:

.. code-block:: sh

  $ ./{birdname}/tests
  $ ./{birdname}/tests/testdata

.. _note:: See also the administration guideline to set up a birdhouse ecosystem.
.. _todo:: add locations of mongodb celery etc...

.. _GitHub: https://github.com/bird-house
.. _`Docker Hub`: https://hub.docker.com/r/birdhouse
