.. _contributing:

Contributing
============

The Birdhouse project openly welcomes contributions
(bug reports, bug fixes, code enhancements/features, etc.).
This document will outline some guidelines on contributing to birdhouse.
As well, the birdhouse :ref:`community` is a great place to get an idea of
how to connect and participate in birdhouse community and development.

Code of Conduct
---------------

Contributors to this project are expected to act respectfully toward others in
accordance with the `OSGeo Code of Conduct`_.

Source code
-----------

The source code of all birdhouse components is available on GitHub_.

Issue tracker
-------------

Please use the issue tracker on GitHub for the corresponding birdhouse component.

WPS client side:

* `Phoenix web application <https://github.com/bird-house/pyramid-phoenix/issues>`_
* `Birdy command line WPS client <https://github.com/bird-house/birdy/issues>`_

WPS server side:

* `Flyingpigeon WPS for climate impact <https://github.com/bird-house/flyingpigeon/issues>`_
* `Hummingbird WPS processes for cdo and compliance checking <https://github.com/bird-house/hummingbird/issues>`_
* `Emu WPS processes for demo and testing <https://github.com/bird-house/emu/issues>`_
* `Malleefowl WPS base processes to access data <https://github.com/bird-house/malleefowl/issues>`_

WPS Security:

* `Twitcher, an WPS security proxy <https://github.com/bird-house/twitcher/issues>`_

Website development
-------------------

The birdhouse website is on http://bird-house.github.io/.
The HTML pages are `maintained on GitHub <https://github.com/bird-house/bird-house.github.io>`_.

Documentation
-------------

Documentation is written in reStructuredText_ and generated with Sphinx_.

* http://sphinx-doc.org/tutorial.html
* http://quick-sphinx-tutorial.readthedocs.io/en/latest/

The documentation is automatically published to ReadTheDocs_ with GitHub webhooks.

The main `documentation`_ (which you are reading now) is the starting point to
get an overview of birdhouse. Each birdhouse component comes with
its own Sphinx documentation and is referenced by the main birdhouse document.

.. _`OSGeo Code of Conduct`: http://www.osgeo.org/code_of_conduct
.. _`documentation`: https://github.com/bird-house/birdhouse-docs
.. _`GitHub`: https://github.com/bird-house
