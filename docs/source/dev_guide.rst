.. _devguide:

Developer Guide
===============

.. contents::
    :local:
    :depth: 2

.. _anaconda:

Birdhouse Anaconda Packages
---------------------------

The installation of the Birdhouse components and especially the processes involve many software dependencies. The core dependencies are of course the WPS related packages like `PyWPS` and `OWSLib` from the GeoPython project. But most dependencies come from the processes itself served by the WPS like `numpy`, `R`, `NetCDF`, `CDO`, `matplotlib`, ... and many more. 

The aim of Birdhouse is to take care of all these dependencies so that the user does not need to install them manually. If these dependencies would only be *pure* Python packages then using the :term:`Buildout` build tool together with the Python package index :term:`PyPi` would be sufficient. But many Python packages have `C` extensions and there are also non-Python packages we need to install like `R` and `netcdflib`.

In this situation the :term:`Anaconda Python distribution` comes helpful. Anaconda has already a lot of Python related packages available for different platforms (Linux, MacOSX, Windows) and there is no compilation needed on the installation host. Anaconda makes it easy to build own packages (*conda recipes*) and to upload them to the free Anaconda server on :term:`Binstar`.

Birdhouse is using Anaconda and it is integrated into the Buildout build tool. The additional *conda recipes* used by Birdhouse are available on `GitHub <https://github.com/bird-house/conda-recipes>`_. The build packages can be installed from the `Birdhouse organisation on Binstar <https://binstar.org/birdhouse>`_. For example if you are already using Anaconda, you can install `CDO` with the following command::

    $ conda install -c birdhouse cdo

If Anaconda would not be available one could also provide these packages from source and compile them on each installation host. Buildout does provide ways to do so. But an initial installation with most of the software used in climate science could *easily take hours*. 

Alternative package manager to Anaconda are for example :term:`Homebrew` (MacOSX only) and :term:`Linuxbrew` (a fork of Homebrew for Linux).

Buildout Recipes provided by Birdhouse
--------------------------------------

:term:`Buildout` has a plugin mechanism to extend the build tool functionality with `recipes <http://www.buildout.org/en/latest/docs/recipe.html>`_. Birdhouse provides a Buildout recipe to install Anaconda packages. There is also a set of recipes to set up Web Processing Service with PyWPS, Nginx, Gunicorn and Supervisor. All these `Buildout recipes are on GitHub <https://github.com/bird-house?query=birdhousebuilder.recipe>`_ and can be `found on PyPi <https://pypi.python.org/pypi?%3Aaction=search&term=birdhousebuilder.recipe&submit=search>`_. 

Here is the list of currently used Buildout recipes by Birdhouse:

* `birdhousebuilder.recipe.conda <https://pypi.python.org/pypi/birdhousebuilder.recipe.conda>`_: A Buildout recipe to install Anaconda packages.
* `birdhousebuilder.recipe.pywps <https://pypi.python.org/pypi/birdhousebuilder.recipe.pywps>`_: A Buildout recipe to install and configure PyWPS Web Processing Service with Anaconda.
* `birdhousebuilder.recipe.pycsw <https://pypi.python.org/pypi/birdhousebuilder.recipe.pycsw>`_: A Buildout recipe to install and configure pycsw Catalog Service (CSW) with Anaconda.
* `birdhousebuilder.recipe.nginx <https://pypi.python.org/pypi/birdhousebuilder.recipe.nginx>`_: A Buildout recipe to install and configure Nginx with Anaconda.
* `birdhousebuilder.recipe.supervisor <https://pypi.python.org/pypi/birdhousebuilder.recipe.supervisor>`_: A Buildout recipe to install and configure supervisor for Anaconda.
* `birdhousebuilder.recipe.docker <https://pypi.python.org/pypi/birdhousebuilder.recipe.docker>`_: A Buildout recipe to generate a Dockerfile for Birdhouse applications.


Writing a WPS process
---------------------

In Birdhouse we are using the :term:`PyWPS` implementation of a :term:`Web Processing Service`. Writing a WPS process in Birdhouse is the same as in PyWPS. The PyWPS documentation has a `tutorial on writing a process <http://pywps.wald.intevation.org/documentation/course/process/index.html>`_. *Please* follow this PyWPS tutorial. 

To get easier started you can install :ref:`Emu <emu:installation>` with some example processes for PyWPS.


 










