.. _dev_guide:

Developer Guidelines
====================

.. contents::
    :local:
    :depth: 3

The Birdhouse project openly welcomes contributions (bug reports, bug fixes, code enhancements/features, etc.). This document will outline some guidelines on contributing to birdhouse. As well, the birdhouse :ref:`communication` is a great place to get an idea of how to connect and participate in birdhouse community and development where everybody is welcome to rise questions and discussions.

For better understanding this section, it is recommended that you are familiar with the :ref:`admin_guide`.

.. _codeofconduct:
Code of Conduct
---------------

.. note: Before we start please be aware that contributors to this project are expected to act respectfully toward others in
accordance with the `OSGeo Code of Conduct`_.

Contribution Workflow
---------------------

.. todo:: The coding guide needs to be updated.

Please find the coding guide in the
`Wiki <https://github.com/bird-house/bird-house.github.io/wiki/Development-Guidelines>`_.


.. _codestyle:
Python Code Style (PEP8)
------------------------

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

.. _writing_functions:

.. todo: guidline for writing functions. Where to place, how to comment.

.. _writing_WPS_process:

Writing a WPS process
---------------------

In birdhouse, we are using the PyWPS_ implementation of a :term:`Web Processing Service`.
Please read the PyWPS `documentation <https://pywps.readthedocs.io/en/master/process.html>`_
on how to implement a WPS process.

.. note:: To get started quickly, you can try the Emu_ WPS with some example processes for PyWPS.

Make your own Bird
..................

We have now a Cookiecutter_ template to create a new bird (PyWPS application).
It is the recommended and fastest way to create your own bird:

https://github.com/bird-house/cookiecutter-birdhouse

.. note:: The cookiecutter is brand-new. Please give feedback and help to improve it.


.. _writing_tests:

Writing tests
-------------

.. todo: missing so far :-)


.. _writing_docs:

Writing documentation
---------------------

Last but not least, a very very important point is to write a good documentation about your work! Each WPS (bird) has a docs folder for this where the documentation is written in reStructuredText_ and generated with Sphinx_.

* http://sphinx-doc.org/tutorial.html
* http://quick-sphinx-tutorial.readthedocs.io/en/latest/

The documentation is automatically published to ReadTheDocs_ with GitHub webhooks.
It is important to keep the :ref:`_codestyle` and write explainations to your functions. There is an auto-api for documentation of functions.
.. todo: explenation of enabling spinx automatic api documentation.

The main `documentation`_ (which you are reading now) is the starting point to
get an overview of birdhouse. Each birdhouse component comes with
its own Sphinx documentation and is referenced by the main birdhouse document.

.. _`OSGeo Code of Conduct`: http://www.osgeo.org/code_of_conduct
.. _`documentation`: https://github.com/bird-house/birdhouse-docs
.. _`GitHub`: https://github.com/bird-house
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _flake8: http://flake8.pycqa.org/en/latest/
