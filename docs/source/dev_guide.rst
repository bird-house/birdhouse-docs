.. _dev_guide:

Developer Guidelines
====================

.. contents::
    :local:
    :depth: 1

.. _codeofconduct:

Code of Conduct
---------------

.. note:: Before we start please be aware that contributors to this project are expected to act respectfully toward others in accordance with the `OSGeo Code of Conduct`_.

Contribution Workflow
---------------------
The Birdhouse project openly welcomes contributions (bug reports, bug fixes, code enhancements/features, etc.). This document will outline some guidelines on contributing to birdhouse. As well, the birdhouse :ref:`communication` is a great place to get an idea of how to connect and participate in birdhouse community and development where everybody is welcome to rise questions and discussions.

Here are some basic guides to smoothly contribute to birdhouse:

.. _source_code:

Source code
...........
The source code of all birdhouse components is available on GitHub_. Respecting the git mechanisms you can fork, clone and pull source-code into your repositories for modification and enhancement. Once your improvement is ready, make a pull request to integrate your work into the origin birdhouse repositories.

.. note:: Please keep your forks close to the origin repositories and don't forget the pull requests.

.. _issuetracker:

Issue tracker
.............

To keep track on the contribution and development, please use the issue tracker on GitHub for the corresponding birdhouse component.


Please find the coding guide in the
`Wiki <https://github.com/bird-house/bird-house.github.io/wiki/Development-Guidelines>`_.

.. _writing_WPS_process:

Writing a WPS process
---------------------

In birdhouse, we are using the PyWPS_ implementation of a :term:`Web Processing Service`.
Please read the `PyWPS documentation <https://pywps.readthedocs.io/en/master/process.html>`_
on how to implement a WPS process.

.. note:: To get started quickly, you can try the Emu_ WPS with some example processes for PyWPS.

.. image:: _images/process_schema_1.png

Another point to think about when designing a process is the possibility of chaining processes together. The result of a process can be a final result or be used as an input for another process. Chaining processes is a common practice but depends on the user you are designing the service for.
Technically, for the development of WPS process chaining, here are a few summary points:

*    the functional code should be modular and provide an interface/method for each single task
*    provide a wps process for each task
*    wps processes can be chained, manually or within the code, to run a complete workflow
*    wps chaining can be done manually, with workflow tools, direct wps chaining or with code scripts
*    a complete workflow chain could also be started by a wps process.

.. image:: _images/wps_chain.png

.. _writing_functions:

Writing functions
-----------------

A Process is calling several functions during the performance. Since WPS is a autonom running process several eventualities needs to be taken into account. If irregularities are occurring, it is a question of the process design if the performance should stop and return an error or continue with may be an modified result.

In practice, the functions should be encapsulated in **try** and **except** calls and appropriate information given to the logfile or shown as a status message. The logger has several options to to influence the running code and the information writing to the logfile:

.. image:: _images/module_chain.png

.. code-block:: python
   :linenos:

   # the following two line needs to be in the beginning of the *.py file.
   # The ._handler will find the appropriate logfile and include timestemps
   # and module information into the log.

   import logging
   LOGGER = logging.getLogger("PYWPS")

   # set a status message
   per = 5  # 5 will be 5% in the status line
   response.update_status('execution started at : {}'.fromat(dt.now()), per)

   try:
       response.update_status('the process is doing something: {}'.fromat(dt.now()),10)
       result = 42
       LOGGER.info('found the answer of life')
   except Exception as ex:
       msg = 'This failed but is obligatory for the output. The process stops now, because: {} '.format(ex)
       LOGGER.error(msg)

   try:
       response.update_status('the process is doing something else : {}'.fromat(dt.now()), 20)
       interesting = True
       LOGGER.info(' Thanks for reading the guidelines ')
       LOGGER.debug(' I need to know some details of the process: {} '.format(interesting)
   except Exception as ex:
       msg = 'This failed but is not obligatory for the output. The process will continue. Reason for the failure: {} '.format(ex)
       LOGGER.exception(msg)

.. _writing_docs:

Writing documentation
---------------------

Last but not least, a very very important point is to write a good documentation about your work! Each WPS (bird) has a docs folder for this where the documentation is written in reStructuredText_ and generated with Sphinx_.

* http://sphinx-doc.org/tutorial.html
* http://quick-sphinx-tutorial.readthedocs.io/en/latest/

The documentation is automatically published to ReadTheDocs_ with GitHub webhooks.
It is important to keep the :ref:`codestyle` and write explanations to your functions. There is an auto-api for documentation of functions.

.. todo:: explanation of enabling spinx automatic api documentation.

The main `documentation`_ (which you are reading now) is the starting point to
get an overview of birdhouse. Each birdhouse component comes with
its own Sphinx documentation and is referenced by the main birdhouse document. Projects using birdhouse components like PAVICS_ or `COPERNICUS Data Store`_ generally have their own documentation as well. To include documentation from external repository here, two custom made sphinx directives can be used. The `gittoctree` directive behaves like a normal table of content directive (`toctree`), but takes as an argument the URL to the git repo and refers to files inside this directory through their full path. The `gitinclude` directive acts like an normal `include` directive, but takes as a first argument the URL to the git repo this file belongs to. For example:

.. code-block:: sphinx
   :linenos:

   Here is the text of the birdhouse main documentation. At the place where you want to integrate
   a part of a remote sphinx documentation stored in a `git` repository you can fetch the docs
   parts and integrated it with a table of content referring to external files:

   .. gittoctree:: https://github.com/Ouranosinc/pavics-sdi.git

      docs/source/arch/backend.rst

   or include an individual file:

   .. gitinclude:: https://github.com/Ouranosinc/pavics-sdi.git docs/source/arch/backend.rst

   The directive will clone and checkout the repository, then include these external files as if
   they were part of the native documentation.

 .. _writing_tests:

 Writing tests
 -------------

 Writing test is an essential part of software development. The WPS templates produced by Cookiecutter_ are already including the initial folders for units tests and basic dependencies in the environment.
 There are two parts of tests:

 * Unit tests:
 python pytest to check the functionality of functions and processes. They are stored in the folder `{bird WPS}/tests` and appropriate test data  `{bird WPS}/tests/testdata`.

 * notebook tests:
 Code examples of the documentation to demonstrate the usage of WPS services. The examples are written in jupyter notebooks and stored in the documentation folder `{bird WPS}/docs/source/notebooks/`


 .. note:: Look at the Emu_ to see examples.


.. _codestyle:

Code Style
-----------

A good start to contribute is an enhancement of existing code with better or new functions. To respect a common coding style, Birdhouse uses PEP8_ checks to ensure a consistent coding style. Currently the following PEP8 rules are enabled in ``setup.cfg``:

.. code-block:: ini

   [flake8]
   ignore=F401,E402
   max-line-length=120
   exclude=tests

See the flake8_ documentation on how to configure further options.

To check the coding style run ``flake8``:

.. code-block:: sh

    $ flake8 emu   # emu is the folder with python code
    # or
    $ make pep8    # make calls flake8

To make it easier to write code according to the PEP8 rules enable PEP8 checking in your editor. In the following we give examples how to enable code checking for different editors.

Atom
....

* Homepage: https://atom.io/
* PEP8 Atom Plugin: https://github.com/AtomLinter/linter-pep8

.. image:: _images/atom-pep8.png


Sublime
.......

* Install package control if you don't already have it: https://packagecontrol.io/installation
* Follow the instructions here to install Python PEP8 Autoformat: https://packagecontrol.io/packages/Python%20PEP8%20Autoformat
* Edit the settings to conform to the values used in birdhouse, if necessary
* To show the ruler and make wordwrap default, open Preferences → Settings—User and use the following rules

.. code-block:: python

   {
    // set vertical rulers in specified columns.
    "rulers": [79],

    // turn on word wrap for source and text
    // default value is "auto", which means off for source and on for text
    "word_wrap": true,

    // set word wrapping at this column
    // default value is 0, meaning wrapping occurs at window width
    "wrap_width": 79
    }

.. todo:: Add PEP8 instructions for more editors: PyCharm, Kate, Emacs, Vim, Spyder.


Environment with conda
----------------------

.. todo:: How to create a conda package


Make your own Bird
------------------

If you are familiar with all the upper chapters you are ready to create your own WPS. The WPS in birdhouse are named after birds, so this section is giving you a guidline of how to make your own bird. Birds are sorted thematically, so before setting up a new one, make sure it is not already covered and just missing some processes and be clear in the new thematic you would like to provide.

We have now a Cookiecutter_ template to create a new bird (PyWPS application).
It is the recommended and fastest way to create your own bird:

https://github.com/bird-house/cookiecutter-birdhouse

.. note:: The cookiecutter is brand-new. Please give feedback and help to improve it.


Release Notes and Versions:
---------------------------

The development of birdhouse is following a release cycle of around three month. Updates of modules are coordinated by the developers over the communication channels (gitter chat or Video Conference).
New releases are documented in the release notes and communicated over the mailing list.
A release of a birdhouse module is taged with a version number and appropriate git repository version branch.

For an orientation of when to release a new version:

* Full version (v1.0) with scientific publication in a reviewed journal
* subversion (v1.1) by major changes
* subsub versions (v1.1.1) by minor changes

out of the release cycles bug fix patches can be released every time ( communication is not mandatory )

* patch v1.1.1_patch1 bugfix

.. _`COPERNICUS Data Store`: https://cds.climate.copernicus.eu/#!/home
.. _`OSGeo Code of Conduct`: http://www.osgeo.org/code_of_conduct
.. _`documentation`: https://github.com/bird-house/birdhouse-docs
.. _`GitHub`: https://github.com/bird-house
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _flake8: http://flake8.pycqa.org/en/latest/
