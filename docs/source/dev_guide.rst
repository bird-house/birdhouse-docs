.. _devguide:

Developer Guide
===============

.. contents::
    :local:
    :depth: 2

.. _anaconda:

Using Anaconda in Birdhouse
---------------------------

The installation of the Birdhouse components and especially the processes involve many software dependencies. The core dependencies are of course the WPS related packages like :term:`PyWPS` and :term:`OWSLib` from the :term:`GeoPython` project. But most dependencies come from the processes itself served by the WPS like `numpy`, `R`, `NetCDF`, `CDO`, `matplotlib`, `ncl`, `cdat`, ... and many more. 

The aim of Birdhouse is to take care of all these dependencies so that the user does not need to install them manually. If these dependencies would only be *pure* Python packages then using the :term:`Buildout` build tool together with the Python package index :term:`PyPi` would be sufficient. But many Python packages have `C` extensions and there are also non-Python packages we need to install like `R` and :term:`NetCDF`.

In this situation the :term:`Anaconda Python distribution` comes helpful. Anaconda has already a lot of Python related packages available for different platforms (Linux, MacOSX, Windows) and there is no compilation needed on the installation host. Anaconda makes it easy to build own packages (*conda recipes*) and to upload them to the free Anaconda server on :term:`Binstar`.

Conda recipes by Birdhouse
~~~~~~~~~~~~~~~~~~~~~~~~~~

Birdhouse is using :term:`Anaconda` to maintain package dependencies. 
Anaconda gives you the possibility to write your own `conda recipes <http://conda.pydata.org/docs/build.html>`_.
In Birdhouse we have written several conda recipes for the packages that were not available on Anaconda.  
These `additional conda recipes by Birdhouse <https://github.com/bird-house/conda-recipes>`_ are available on :term:`GitHub`. 
Some of the missing packages are: PyWPS, OWSLib, CDO, ocgis/icclim, cfchecker, nginx, ...

Anaconda provides a free Anaconda Server on :term:`Binstar`. Here you can upload your builded conda packages for different platforms (Linux, MacOX, Windows). These packages are then available for installation with the :term:`conda` installer.

`Birdhouse has a Binstar organisation <https://binstar.org/birdhouse>`_ where all conda packages are collected which are 
builded from the conda recipes on GitHub. These packages can be installed with the :term:`conda` installer using the `birdhouse` channel.
For example if you are already using Anaconda, you can install `CDO` with the following command::

    $ conda install --channel birdhouse cdo

Building conda packages
~~~~~~~~~~~~~~~~~~~~~~~

There are several ways to build conda packages and upload them to Binstar.

* You can `build packages locally <http://docs.binstar.org/conda.html>`_ and upload them with the Binstar command line tool.
* You can also `build packages remotely on Binstar <http://docs.binstar.org/draft/examples.html#SubmitYourFirstBuild>`_. Additionally you can set a GitHub Webhook so that on each commit of your recipe a build will be run on Binstar. 
* The remote build on Binstar are done using Docker images. The `Binstar docker image for Linux-64 <https://registry.hub.docker.com/u/binstar/linux-64/>`_ is available on :term:`Docker Hub`.  

In Birdhouse we usually use the remote build on Binstar which is triggered by commits to GitHub. 
But sometimes the docker image for Linux-64 provided by Binstar fails for some packages. 
That is why `Birdhouse has in addition its own Linux-64 build image <https://registry.hub.docker.com/u/birdhouse/binstar-linux-64/>`_ which is based on the Binstar image. 
The `Dockerfile for this image <https://github.com/bird-house/birdhouse-build/tree/master/docker/binstar-linux-64>`_ is on GitHub.
 

Anaconda Alternatives
~~~~~~~~~~~~~~~~~~~~~

If Anaconda would not be available one could also provide these packages from source and compile them on each installation host. Buildout does provide ways to do so. But an initial installation with most of the software used in climate science could *easily take hours*. 

Alternative package manager to Anaconda are for example :term:`Homebrew` (MacOSX only) and :term:`Linuxbrew` (a fork of Homebrew for Linux).

Using Buildout in Birdhouse
---------------------------

Birdhouse uses the :term:`Buildout` build tool to install and configure all Birdhouse components (:term:`Phoenix`, :term:`Malleefowl`, :term:`Emu`...). The main configuration file is ``buildout.cfg`` which is in the root folder of the application. 
As an example have a look at the `buildout.cfg from Emu <https://github.com/bird-house/emu/blob/master/buildout.cfg>`_. 

Before building an application with Buildout you have an initial bootstrap step::

    $ python bootstrap-buildout.py -c buildout.cfg

This will generate the ``bin/buildout`` script.
Now you can build the application::

    $ bin/buildout -c buildout.cfg

The default configuration in the ``buildout.cfg`` should always work to run your application on ``localhost`` with default ports. You can customize the configuration by editing the ``custom.cfg`` which extends and overwrites the settings of ``buildout.cfg``. You may have a look at the
`custom.cfg example of Emu <https://github.com/bird-house/emu/blob/master/custom.cfg.example>`_. So, instead of using ``buildout.cfg`` you should use ``custom.cfg`` for the build::

    $ bin/buildout -c custom.cfg

For convenience Birdhouse has a Makefile which hides all these steps. If you want to build an application you just need to run::

    $ make install

See the `Makefile example of Emu <https://github.com/bird-house/emu/blob/master/Makefile>`_
For more details see the :ref:`installation` section and the :ref:`Makefile documentation <bootstrap:makefile>`.


Buildout Recipes by Birdhouse
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:term:`Buildout` has a plugin mechanism to extend the build tool functionality with `recipes <http://www.buildout.org/en/latest/docs/recipe.html>`_. Buildout can handle Python dependencies by its own. But in Birdhouse we install most dependencies with Anaconda. We are using a Buildout extension to install conda packages with Buildout. Buildout does use these Python packages instead of downloading them from :term:`PyPi`. 
There is also a set of recipes to set up Web Processing Service with :term:`PyWPS`, :term:`Nginx`, :term:`Gunicorn` and :term:`Supervisor`. 
All these `Buildout recipes are on GitHub <https://github.com/bird-house?query=birdhousebuilder.recipe>`_ and can be `found on PyPi <https://pypi.python.org/pypi?%3Aaction=search&term=birdhousebuilder.recipe&submit=search>`_. 

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


 










