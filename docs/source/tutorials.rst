.. _tutorials:

**********
Tutorials
**********
.. contents::
    :local:
    :depth: 3


.. warning::
    Work in progress. Examples will come soon.

This is a collection of tutorials and examples covering to show usage of WPS services but is also covering general data management with an focus on sustainable development.

If you are a newcommer, you might have to go through a basic python tutorial first:
.. todo:: Python tutorial

Climate data management
-----------------------
**general Tutorial** about climate and related data handling.

* esfg-python client


WPS general usage
-----------------
General concepts and tutorials for pyWPS:

* `PyWPS 4.0.0 Slides <http://www.slideshare.net/jachym/pywps400>`_
* `PyWPS Documentation <https://pywps.readthedocs.io/en/master/process.html>`_

You can connect to a WPS service in the following ways:

* using a command-line tool in your terminal.
* using a web based application from your browser.
* using a Python library from a jupyter notebook or your Python scripts.

.. toctree::
   :maxdepth: 1

   tutorial_wps

.. todo:: birdy example
.. todo:: Screen-shot of Phoenix


WPS services of birdhouse
-------------------------

* Climate Indices (finch):

.. gittoctree:: https://github.com/bird-house/finch.git

   docs/source/notebooks/index.rst


.. gitinclude:: https://github.com/bird-house/finch/blob/master/docs/source/notebooks/index.rst


* :ref:`Emu Example with Docker <emu:tutorial>`
* :ref:`Example with Birdy WPS command line tool <birdy:tutorial>`
