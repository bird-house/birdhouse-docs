.. _framework:

************
Architecture
************

.. contents::
    :local:
    :depth: 2


Birdhouse is organized in separate stand-alone software components. Most components are named after birds, which gives the  project its name birdhouse. The components can be categorized into :ref:`client_components`, i.e. tools for end-users, and :ref:`server_components`, i.e. back-end elements of the architecture.


.. _framework_structure:

Framework structure
-------------------

There are several WPS services. Malleefowl_ is the main one for the Phoenix_ client.
Malleefowl is used to search, download (with caching) ESGF data and to retrieve certificates.
Malleefowl has also a workflow engine (dispel4py_) to chain WPS processes.

The results of the WPS processes are stored on the file system and are accessible via URL (with a token id).
Results can be shown on a Map using a Web Mapping Service (ncWMS, adagucserver).
The PyCSW Catalog Service is used to register WPS services and also to publish WPS outputs.
Published results in the PyCSW can also used as input source for processes again.

ESGF_ is currently the main climate data resource (but more resources are possible).
ESGF Solr-index is used to find ESGF data. The ESGF identity provider with OpenIDs and X509 certificate is used for authentication.

WPS serivces can be accessed through web-applications like Phoenix or from scripts.

.. image:: _images/birdhouse-framework.png

.. note:: See also the :ref:`Publications and Presentations <publications>` for more information and details.


.. _client_components:

Client Side Components
----------------------

* `Phoenix`_: a web-based WPS client with ESGF data access
* `Birdy`_: a WPS command line client and native library
* `Weaver`_: provides a
  `Python client and command line interface <https://pavics-weaver.readthedocs.io/en/latest/cli.html>`_
  for *OGC API - Processes*, *Common Workflow Language* (CWL), and remote WPS providers.

.. _server_components:

Server Side Components
----------------------

WPS services for climate data analysis:

* Emu_: some example WPS processes for demo
* Flyingpigeon_: Testbed for new process development
* `Black Swan`_: services for the extreme weather event assessments
* Hummingbird_: provides cdo and compliance-checker as a service
* Finch_: services for climate indices calculation
* Pelican_: Supporting ESGF compute API
* Kingfisher_: Services for Earth-Observation data analysis

Many climate analysis operations are implemented using OpenClimateGIS_
including the `python package icclim <http://icclim.readthedocs.io/en/latest/>`_.

Supporting Services and libraries:

* Twitcher_: an OWS Security Proxy
* Malleefowl_: access to climate data (ESGF, ...) as a service
* Eggshell_: provides common functionality for Birdhouse WPS services
* Weaver_: provides support for *OGC API - Processes*, *Common Workflow Language* (CWL) and remote WPS Workflows

You can find the source code of all birdhouse components on GitHub_.
Docker images with birdhouse components are on `Docker Hub`_

Files and Folders
-----------------

This is an overview of folder structure and important files for :ref:`administration of a server-side <admin_guide>` birdhouse ecosystem.

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

.. _GitHub: https://github.com/bird-house
.. _`Docker Hub`: https://hub.docker.com/r/birdhouse
