.. _tutorials:

**********
Tutorials
**********
<<<<<<< HEAD

This is a collection of tutorials and examples covering to show usage of WPS services but is also covering general data management with an focus on sustainable development.
=======
.. contents::
    :local:
    :depth: 3

To guide you through the learning curve of installation modules of birdhouse and set up an running birdhouse ecosystem, administer the server-side birdhouse components or even improve and develop your own specific functions, here are some general tutorials. This is a collection of tutorials and examples covering to show usage of WPS services but is also covering general data management with an focus on sustainable development.
>>>>>>> guidelines

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

   tutorial_firststepps
   _tutorials/CMIP_resolution.ipynb


First stepps with WPS
----------------------

Environment with conda
......................

.. todo:: How to create a conda package


Make your own Bird
..................

If you are familiar with all the upper chapters you are ready to create your own WPS. The WPS in birdhouse are named after birds, so this section is giving you a guidline of how to make your own bird. Birds are sorted thematically, so before setting up a new one, make sure it is not already covered and just missing some processes and be clear in the new thematic you would like to provide.

We have now a Cookiecutter_ template to create a new bird (PyWPS application).
It is the recommended and fastest way to create your own bird:

https://github.com/bird-house/cookiecutter-birdhouse

.. note:: The cookiecutter is brand-new. Please give feedback and help to improve it.



WPS services of birdhouse
-------------------------

* Climate Indices (finch):


.. _python_guide:

Python syntax:
==============

.. code:: ipython3

    """Python WPS execute"""

    from owslib.wps import WebProcessingService, monitorExecution
    from os import system


.. code:: ipython3

   tutorial_wps

First stepps with WPS services of birdhouse
-------------------------------------------

The following section are tutorials of the different components of birdhouse.

Hello World WPS (emu):
......................

* :ref:`Emu Example with Docker <emu:tutorial>`

WPS client (birdy):
...................

* :ref:`Example with Birdy WPS command line tool <birdy:tutorial>`

Climate Indices (finch):
........................

WPS finch is providing services to calculate climate indices widely used in climate change adaptation planing processes.

.. gittoctree:: https://github.com/bird-house/finch.git

  docs/source/notebooks/index.rst


.. gitinclude:: https://github.com/bird-house/finch/blob/master/docs/source/notebooks/index.rst


Hydrological models (raven):
............................

WPS raven is providing hydrological models for e.g. hydro-power controlling and sustainable planing

.. gittoctree:: https://github.com/Ouranosinc/raven.git

   docs/source/notebooks/index.rst


.. gitinclude:: https://github.com/Ouranosinc/raven/blob/master/docs/source/notebooks/index.rst


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
