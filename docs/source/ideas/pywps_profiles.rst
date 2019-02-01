.. _pywps_profiles:

PyWPS Profiles
==============

.. contents::
    :local:
    :depth: 2

.. warning::
    Work in progress.


Motivation
----------

It happens quite often that we have a set of processes with common input (and output) parameters.
In WPS the process signature (inputs+outputs) is called a `WPS profile`_.
In the following we show examples how to avoid *copy+paste* of these process parameters.

Python Mixins
-------------

One could use Python *mixin classes* to define a commonly used profile
which can be adapted by each individual process.

See how a mixin class looks like:

https://www.ianlewis.org/en/mixins-and-python

See notebook examples how it could be used with PyWPS:

https://nbviewer.jupyter.org/github/bird-house/notebooks/blob/master/pywps-profiles/notebooks/process_mixin.ipynb

Python Decorators
-----------------

We can also use function decorator to define a WPS profile for PyWPS.

See how a function decorator looks like:

https://krzysztofzuraw.com/blog/2016/python-class-decorators.html

Here are some notebook examples how it could be used with PyWPS:

* notebooks: https://nbviewer.jupyter.org/github/bird-house/notebooks/blob/master/pywps-profiles/notebooks/process_decorator.ipynb
* Emu subset with ESGF-API: https://github.com/bird-house/emu/blob/esgfwps/emu/processes/wps_esgf_subset.py

Simple Alternative: Shared Profile Module/Class
-----------------------------------------------

Relatively few developers will be familiar with the concepts of *mixins* and *decorators*.
In other words, it might look a bit too much like magic.
We could also simply create a module with all the common inputs and outputs used
throughout the different WPS processes (`wpsio.py`).
For a given Process definition, one then just import `wpsio` and refer to the objects
in the inputs and outputs fields of the `Process.init` method.

See for example:

https://github.com/Ouranosinc/raven/blob/master/raven/processes/wps_regionalisation.py

Here is a notebook showing this approach which includes also an optional decorator:

https://nbviewer.jupyter.org/github/bird-house/notebooks/blob/master/pywps-profiles/notebooks/process_simple_profile_and_decorator.ipynb


.. _WPS profile: http://geoprocessing.info/wpsdoc/FAQ#profile
