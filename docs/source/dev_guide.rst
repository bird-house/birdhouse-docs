.. _dev_guide:


Developer Guidelines
====================

.. contents::
    :local:
    :depth: 3

Guidelines and tutorials for Developers to include new components to birdhouse or enhance existing functionality.


Make your own Bird
------------------

We have now a Cookiecutter_ template to create a new bird (PyWPS application).
It is the recommended and fastest way to create your own bird:

https://github.com/bird-house/cookiecutter-birdhouse

.. note:: The cookiecutter is brand-new. Please give feedback and help to improve it.

.. _writing_WPS_process:

Writing a WPS process
---------------------

In birdhouse, we are using the PyWPS_ implementation of a :term:`Web Processing Service`.
Please read the PyWPS `documentation <https://pywps.readthedocs.io/en/master/process.html>`_
on how to implement a WPS process.

.. note:: To get started quickly, you can try the Emu_ WPS with some example processes for PyWPS.

.. _conda:

Python Code Style (PEP8)
------------------------

Birdhouse uses PEP8_ checks to ensure a consistent coding style. Currently the following PEP8 rules are enabled
in ``setup.cfg``:

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

To make it easier to write code according to the PEP8 rules enable PEP8 checking in your editor.
In the following we give examples how to enable code checking for different editors.

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

Contribution Workflow
---------------------

.. todo:: The coding guide needs to be updated.

Please find the coding guide in the
`Wiki <https://github.com/bird-house/bird-house.github.io/wiki/Development-Guidelines>`_.



.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _flake8: http://flake8.pycqa.org/en/latest/
