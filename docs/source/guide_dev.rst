.. _guide_guide:

<<<<<<< HEAD
Software development
====================
=======
Coding guide
============

>>>>>>> guidelines

.. contents::
    :local:
    :depth: 1



Here are some basic guides to smoothly contribute to birdhouse:

.. _source_code:

Source code
...........
The source code of all birdhouse components is available on GitHub_. Respecting the git mechanisms you can fork, clone and pull source-code into your repositories for modification and enhancement. Once your improvement is ready, make a pull request to integrate your work into the origin birdhouse repositories.

.. note:: Please keep your forks close to the origin repositories and don't forget the pull requests.

Git contribution
................

.. note::  Please find the git contribution guide in the `Wiki <https://github.com/bird-house/bird-house.github.io/wiki/Development-Guidelines>`_.

.. _issuetracker:

Issue tracker
.............

To keep track on the contribution and development, please use the issue tracker on GitHub for the corresponding birdhouse component.


.. _codestyle:

Code Style
..........

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
----

* Homepage: https://atom.io/
* PEP8 Atom Plugin: https://github.com/AtomLinter/linter-pep8

.. image:: _images/atom-pep8.png


Sublime
-------

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


Release Notes and Versions
..........................

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
.. _`documentation`: https://github.com/bird-house/birdhouse-docs
.. _`GitHub`: https://github.com/bird-house
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _flake8: http://flake8.pycqa.org/en/latest/
