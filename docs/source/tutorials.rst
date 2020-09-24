.. _tutorials:

**********
Tutorials
**********

This is a collection of tutorials and examples covering to show usage of WPS services but is also covering general data management with an focus on sustainable development.

.. contents::
    :local:
    :depth: 1

Introduction
------------

Data for sustainable Development
................................


First stepps with climate data
------------------------------

.. toctree::
   :maxdepth: 2

   _tutorials/CMIP_resolution


First stepps with WPS
----------------------

.. toctree::
   :maxdepth: 2

   tutorial_wps

First stepps with WPS services of birdhouse
-------------------------------------------

The following section are tutorials of the different components of birdhouse.

Beginner WPS (emu):
...................

* :ref:`Emu Example with Docker <emu:tutorial>`

WPS client (birdy):
...................

* :ref:`Example with Birdy WPS command line tool <birdy:tutorial>`

Climate Indices (finch):
........................

Birdhouse is providing services to calculate climate indices widely used in climate change adaptation planing processes.

.. gittoctree:: https://github.com/bird-house/finch.git

  docs/source/notebooks/index.rst


.. gitinclude:: https://github.com/bird-house/finch/blob/master/docs/source/notebooks/index.rst


Combining services
------------------

.. todo:: Chaining birds
.. todo:: calling external services


Server administration
---------------------

.. toctree::
   :maxdepth: 1

   tutorial_install
   tutorial_admin
