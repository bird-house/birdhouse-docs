.. Birdhouse documentation master file, created by
   sphinx-quickstart on Tue Mar 10 15:22:06 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

Birdhouse is a collection of :term:`Web Processing Service` (WPS) related
Python components to support data processing in the climate science
community. The aim of birdhouse is to make the usage of WPS easy. Most
of the :term:`OGC`/:term:`WPS` related software comes from the :term:`GeoPython` project. 

Birdhouse is the home of Web Processing Services used in climate science and components to support them (the birds).

WPS client side:

* `Phoenix`_: a web-based WPS client with ESGF data access
* `Birdy`_: a WPS command line tool

WPS supporting services and libraries:

* `Twitcher`_: a simple OWS Security Proxy
* `Malleefowl`_: access to climate data (ESGF, ...) as a service and library

WPS services and libraries with algorithms used in climate science analysis: 

* `Flyingpigeon`_: services for the climate impact community
* `Hummingbird`_: provides cdo and cfchecker as a service
* `Dodrio <https://github.com/bird-house/dodrio>`_: WPS for KIT
* `Emu`_: some example WPS processes


You can find the source code of all birdhouse components on
`our GitHub page <https://github.com/bird-house>`_. 
:term:`Conda` packages for birdhouse are available on the `birdhouse channel <https://anaconda.org/birdhouse>`_ on Binstar.
:term:`Docker` images with birdhouse components are on `Docker Hub <https://hub.docker.com/r/birdhouse/>`_ 

Getting started
===============

.. toctree::
   :maxdepth: 2

   overview
   installation
   tutorial
   admin_guide
   dev_guide
   contributing
   faq
   glossary
   release_notes
   roadmap
   appendix

Presentations & Blog Posts
==========================


* `ESGF F2F 2016 at Washington <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-esgf-f2f-2016/birdhouse-esgf-f2f-2016_dkrz.pdf>`_
* `FOSS4G 2016 at Bonn <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-foss4g-2016/Hempelmann_foss4g2016.pdf>`_
* `EGU 2016 at Vienna <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-egu-2016/EGU-Processing-DKRZ.pdf>`_
* `ICRC-CORDEX 2016 <https://github.com/bird-house/birdhouse-docs/blob/master/slides/Hempelmann_CORDEX2016_datatoinformation.pdf>`_
* Model Animation LSCE
* `Talk on USGS WebEx 2016/02/18 <https://my.usgs.gov/confluence/pages/viewpage.action?pageId=542482181>`_
* `Paris Coding Spring 2015 at IPSL <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-architecture/birdhouse-architecture.pdf>`_
* `EGI Community Forum 2014 at Helsinki <https://indico.egi.eu/indico/event/1994/session/23/contribution/134>`_
* Prag
* CSC 2.0 Hamburg
* Vienna
* LSDMA

License Agreement
=================

Birdhouse components are distributed under the `Apache License, Version 2.0 <https://opensource.org/licenses/Apache-2.0/>`_.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

