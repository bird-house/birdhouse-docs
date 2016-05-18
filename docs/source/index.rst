.. Birdhouse documentation master file, created by
   sphinx-quickstart on Tue Mar 10 15:22:06 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Introduction
============

Birdhouse is a collection of :term:`Web Processing Service` (WPS) related
Python components to support data processing in the climate science
community. The aim of Birdhouse is to make the usage of WPS easy. Most
of the :term:`OGC`/:term:`WPS` related software comes from the :term:`GeoPython` project. 

Birdhouse is the home of Web Procssing Services used in climate science and components to support them (the birds).

WPS client side:

* :ref:`Phoenix <phoenix:introduction>`: a web-based WPS client with ESGF data access
* :ref:`Birdy <birdy:introduction>`: a WPS command line tool

WPS supporting services and libraries:

* :ref:`Twitcher <twitcher:introduction>`: a simple OWS Security Proxy
* :ref:`Malleefowl <malleefowl:introduction>`: access to climate data (ESGF, ...) as a service and library

WPS services and libraries with algorithms used in climate science analysis: 

* :ref:`Flyingpigeon <flyingpigeon:introduction>`: services for the climate impact community
* :ref:`Hummingbird <hummingbird:introduction>`: provides cdo and cfchecker as a service
* `Dodrio <https://github.com/bird-house/dodrio>`_: WPS for KIT
* :ref:`Emu <emu:introduction>`: some example WPS processes


You can find the source code of all Birdhouse components on
`our GitHub page <https://github.com/bird-house>`_. 
:term:`Conda` packages for Birdhouse are available on the `birdhouse channel <https://anaconda.org/birdhouse>`_ on Binstar.
:term:`Docker` images with Birdhouse components are on `Docker Hub <https://hub.docker.com/r/birdhouse/>`_ 

Getting started
===============

.. toctree::
   :maxdepth: 2

   overview
   installation
   tutorial
   dev_guide
   contributing
   faq
   glossary
   release_notes
   roadmap
   appendix

Presentations & Blog Posts
==========================

* `ICRC-COEDEX 2016 <https://github.com/bird-house/birdhouse-docs/blob/master/slides/Hempelmann_CORDEX2016_datatoinformation.pdf>`_
* Model Animation LSCE
* `Talk on USGS WebEx 2016/02/18 <https://my.usgs.gov/confluence/pages/viewpage.action?pageId=542482181>`_
* `Paris Coding Spring at IPSL <https://github.com/bird-house/birdhouse-docs/blob/master/slides/birdhouse-architecture/birdhouse-architecture.pdf>`_
* Helsinki
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

