.. _roadmap:

=======
Roadmap
=======

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
  - Token should be part of the url http://localhost/wps/emu/auhbgt3n or http://localhost/wps/emu?request=getcapabilities&token=auhbgt3n
  - using a security proxy service in front of WPS servers.

Docs & Testing
--------------

* tests:

  - improved unit tests
  - continous integration with github+travisCI
  - complete install tests with docker builds

* complete sphinx documentation
* need a better overview of the components
* simple understable image of what WPS is good for
