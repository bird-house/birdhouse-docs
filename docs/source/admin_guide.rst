.. _admin_guide:

Administrator Guidelines
========================

.. contents::
    :local:
    :depth: 2


.. warning:: This section needs is outdated and needs to be rewritten!

.. _birdhouse_ecosystem:

Set up a birdhouse ecosystem server
-----------------------------------

If you are already familiar with installing single standalone WPS (follow the :ref:`installation` guides in the documentations of e.g. emu), then you are ready to set up a birdhouse containing flyingpigeon (providing scientific analyses methods), malleefowl (to search and fetch data) and the pheonix (a graphic interface for a web browser including a WMS).

General Remarks
~~~~~~~~~~~~~~~

| Check the :ref:`requirements` of your system!
| The installation is done as **normal user**, root rights are causing conflicts.


Prepare Installation
~~~~~~~~~~~~~~~~~~~~

It is recommended to collect the repositories in a separate folder (e.g. birdhouse, but can have a name of your choice)::

  $ mkdir birdhouse
  $ cd birdhouse


Get the source code from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: ini

  $ git clone https://github.com/bird-house/flyingpigeon.git
  $ git clone https://github.com/bird-house/pyramid-phoenix.git
  $ git clone https://github.com/bird-house/malleefowl.git

Run Installation
~~~~~~~~~~~~~~~~

You can run the installation with default settings.
It will create a conda environment and deploy all required software dependencies there.

.. note:: Read the *changing the default configuration* if you want to customize the configuration.

In **all** of the tree folders (malleefowl, flyingpigeon and pyramid-phoenix) run::

  $ make install

This installation will take some minutes to fetch all dependencies and install them into separate conda environments.

Start the Services
~~~~~~~~~~~~~~~~~~

in **all** of the birds run::

  $ make start


Launching the Phoenix Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the services are running, you can launch the GUI in a common web browser. By default, phoenix is set to port 8081::

  firefox http://localhost:8081

or::

  firefox https://localhost:8443/

Now you can log in (upper right corner) with your Phoenix password created previously.
Phoenix is just a graphical interface with no more function than looking nice ;-).

Register a service in Phoenix Web App
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: Please read the `Phoenix documentation <https://pyramid-phoenix.readthedocs.io/en/latest/user_guide.html#>`_

Your first administration step is to register *flyingpigeon* as a service.
For that, log in with your phoenix password.
In the upper right corner is a tool symbol to open the `settings`.
Click on `Services` and the `Register a Service`.

Flyingpigeon is per default on port 8093.

The appropriate url is::

  http://localhost:8093/wps

Provide service title and name as you like:
* Service Title: Flyingpigeon
* Service Name: flyingpigeon

check `Service Type`: `Web Processing Service` (default) and register.

Optionally, you can check `Public access?`, to allow unregistered users to launch jobs. (**NOT recommended**)

Launching a Job
~~~~~~~~~~~~~~~

Now your birdhouse ecosysem is set up.
The also installed malleefowl is already running in the background and will do a lot of work silently.
There is **no need to register malleefowl** manually!

Launching a job can be performed as a process (Process menu) or with the wizard. To get familliar with the processes provided by each of the birds, read the approriate documentation for each of the services listed in the `overview: <http://birdhouse.readthedocs.io/en/latest/index.html>`_

Changing the default configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. _note: files and folder section (architecture chapter)

You can customize the configuration of the service. Please read the documentation, for example:

* `Phoenix documentation <https://pyramid-phoenix.readthedocs.io/en/latest/configuration.html>`_
* `Flyingpigeon documentation <https://flyingpigeon.readthedocs.io/en/latest/configuration.html>`_

Furthermore, you might change the hostname (to make your service accessible from outside), ESGF-node connection,
the port or the log-level for more/less information in the administrator logfiles.
Here is an example `pyramid-phoenix/custom.cfg`:

.. code-block:: ini

  [settings]
  hostname = localhost
  http-port = 8081
  https-port = 8443
  log-level = DEBUG
  # run 'make passwd' and to generate password hash
  phoenix-password = sha256:513....
  # generate secret
  # python -c "import os; print(''.join('%02x' % ord(x) for x in os.urandom(16)))"
  phoenix-secret = d5e8417....30
  esgf-search-url = https://esgf-data.dkrz.de/esg-search
  wps-url = http://localhost:8091/wps


Update Phoenix Password
~~~~~~~~~~~~~~~~~~~~~~~

To be able to log into the Phoenix GUI once the services are running, it is necessary to generate a password:
go into the pyramid-phoenix folder and run::

  $ make passwd

This will automatically write a password hash into pyramid-phoenix/custom.cfg

.. _backups:

Backups
--------

See the `mongodb documentation <https://docs.mongodb.com/manual/core/backups/>`_ on how to backup the database.
With the following command you can make a dump of the ``users`` collection of the Phoenix database::

    $ mongodump --port 27027 --db phoenix_db --collection users

Asking for Support
------------------

In case of questions or trouble shooting, feel welcome to join
the `birdhouse chat <https://gitter.im/bird-house/birdhouse>`_
and get into contact with the developers directly.
