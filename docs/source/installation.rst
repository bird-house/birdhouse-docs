.. _installation:

Installation
============

.. contents::
    :local:
    :depth: 2

Birdhouse consists of several components like :ref:`Malleefowl <malleefowl:introduction>` and :ref:`Emu <emu:introduction>`. Each of them can be installed individually. The installation is done using the Python-based build system :term:`Buildout`. Most of the dependencies are maintained in the :term:`Anaconda Python distribution`. For convience each Birdhouse component has a :ref:`Makefile <bootstrap:makefile>` to ease the installation so you don't need to know how to call the Buildout build tool.

Requirements
------------

Birdhouse uses :term:`Anaconda Python distribution` for most of the dependencies. If Anaconda is not already installed it will be installed during the installation process. Anaconda has packages for Linux, MacOSX and Windows. But not all packages used by Birdhouse are already available in the default package channel of Anaconda. The missing packages are supplied by Birdhouse on :term:`Binstar`. But we currently maintain only packages for Linux 64-bit and partly for MacOSX.

So the short answer to the requirements is: **you need a Linux 64-bit installation**. 

Birdhouse is currently used on Ubuntu 14.04 and CentOS 6.x. It should also work on Debian, LinuxMint and Fedora.

Birdhouse is also installing a few system packages using `apt-get` on Debian based distributions and `yum` on RedHat/CentOS based distributions. For this you need a user account with `sudo` permissions. Installing system packages can be done in a separate step. So your installation user does not need any special permissions. All installed files will go into a Birdhouse Anaconda environment in the home folder of the installation user.

Installing from source
----------------------

The installation of Birdhouse components from source is basically a three-liner. Here is an example for the Emu WPS service::

    $ git clone https://github.com/bird-house/emu.git
    $ cd emu
    $ make

All the Birdhouse components follow the same installation pattern. If you want to see all the options of the `Makefile` then type::
 
    $ make help 

You will find more information about these options in the :ref:`Makefile documentation <bootstrap:makefile>`.

Read the documention of each Birdhouse component for the details of the installation and how to configure the components. The :ref:`Birdhouse bootstrap documentation <bootstrap:introduction>` gives some :ref:`examples <bootstrap:examples>` on the different ways of the installation.

On the WPS client side we have:

* :ref:`Phoenix <phoenix:installation>`: a Pyramid web application.
* :ref:`Birdy <birdy:installation>`: a simple WPS command line tool.

On the WPS server side we have:

* :ref:`Malleefowl <malleefowl:installation>`: providing base WPS services to access data.
* :ref:`Flyingpigeon <flyingpigeon:installation>`: providing WPS services for the climate impact community.
* :ref:`Hummingbird <hummingbird:installation>`: providing WPS services for CDO and climate metadata checks.
* :ref:`Emu <emu:installation>`: just some WPS processes for testing.

Nginx, gunicorn and supervisor
------------------------------

Birdhouse setups a :term:`PyWPS` server (and also the Phoenix web application) using :term:`Buildout`. We use the :term:`Gunicorn` HTTP application server (similar to Tomcat for Java servlet applications ) to run these web applications with the :term:`WSGI` interface. In front of the Gunicorn application server we use the :term:`Nginx` HTTP server (similar to Apache web server). All these web services are started/stopped and monitored by a :term:`Supervisor` service. 

See the following image on how this looks like:

.. image:: _images/WsgiApp.png

When installing a Birdhouse WPS service you don't need to care about this setup. This is all done by Buildout and using some extensions provided by Birdhouse. 

The Makefile of a Birdhouse application has convenience targets to start/stop a WPS service controlled by Supervisor and to check the status::

    $ make start    # start wps service
    $ make stop     # stop wps service
    $ make status   # show status of wps service
    Supervisor status ...
    /home/pingu/.conda/envs/birdhouse/bin/supervisorctl status
    emu                              RUNNING   pid 25698, uptime 0:00:02
    malleefowl                       RUNNING   pid 25702, uptime 0:00:02
    mongodb                          RUNNING   pid 25691, uptime 0:00:02
    nginx                            RUNNING   pid 25699, uptime 0:00:02
    phoenix                          RUNNING   pid 25694, uptime 0:00:02
    pycsw                            RUNNING   pid 25700, uptime 0:00:02
    tomcat                           RUNNING   pid 25693, uptime 0:00:02


You can also use the Supervisor monitor web service which by default is available on port http://localhost/9001. The Supervisor monitor app looks like in the following screenshot.

.. image:: _images/supervisor-monitor.png

.. _docker:

Using Birdhouse with Docker
---------------------------

An alternative way to install and deploy Birdhouse Web Processing Services is using :term:`Docker`. The Birdhouse WPS servers are available as Docker image on `Docker Hub <https://registry.hub.docker.com/repos/birdhouse/>`_. See an example on how to use them with the :ref:`Emu WPS Docker image <emu:tutorial>`

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




 




