.. _roadmap:

=======
Roadmap
=======

Milestone December 2015
=======================

* `prototype for wps security proxy <https://github.com/bird-house/twitcher/>`_
* `update ncWMS2 and adagucserver wms <https://github.com/bird-house/birdhousebuilder.recipe.adagucserver>`_
* `update sphinx with api references <https://github.com/bird-house/birdhousebuilder.recipe.sphinx>`_
* `improved birdy command line (https, argcomplete) <https://github.com/bird-house/birdy>`_
* caching of wps requests
* deployment with docker using docker-compose
* `minimal bird example and skeleton function <https://github.com/bird-house/babybird>`_
* unit tests with sample netcdf data
* `wps decorator <https://github.com/bird-house/malleefowl/issues/16>`_
* enable wps for `apache-climate <https://github.com/apache/climate>`_ processes
* try `sci-wms <https://github.com/sci-wms/sci-wms>`_ web map service

Milestone March 2015
====================

* move docs to readthedocs
* birdhouse overview
* presentation at LSDMA in Berlin


Long-term TODO List
===================

Security
--------

* using OAuth for login
* secure WPS service:

  - wps client and services should not be changed
  - using OAuth Token generation
  - Token should be part of the url ``http://localhost/wps/emu/auhbgt3n`` or ``http://localhost/wps/emu?request=getcapabilities&token=auhbgt3n``
  - using a security proxy service in front of WPS servers.
  - `GetCapabilities` and `DescribeProcess` should be available without a security token.

Data Sources
------------

* OpenStack

  - using python swift client

* PyCSW:

  - already there but needs to be refactored
  - CSW is used for publishing results

* ESGF/Thredds:

  - opendap without aggregations (mostly not available)

* Observational Climate Data:

  - which are available for public access and usage (license issuses)

* local file archives:

  - make them searchable ... pattern matching ... index service ...

* CERA climate database
* OGC data services like WCS and SOS, ...

Web Processing Service
----------------------

* usage of other WPS implementations: COWS, GeoServer, Zoo, ...

  - process integration interface (with python decorators) which generates the integration code for other WPS services.

* extensions: cancel (comes with wps 2.0), dry-run, ... cows and maybe geoserver have some of these
* caching process execution: cows has cachings ... but should be independent of the wps implementation  

Deployment
----------

* deployment with saltstack and/or docker ...

Highload Processing
-------------------

* integration of scheduler ... slurm ... (cows has an example for that)
* using load balancing ...

Docs & Testing
--------------

* tests:

  - improved unit tests
  - continous integration with github + travisCI + binstar + docker
  - complete install tests with docker builds

* complete sphinx documentation
* need a better overview of the components
* simple understable image of what WPS is good for
