
.. _projects:

Project examples
================

.. contents::
    :local:
    :depth: 1

The birdhouse :ref:`framework is modular organized <framework_structure>` to enable a flexible architecture design depending on the projects needs. Due to the OCG Standard, software components non-birdhouse components can be combined for interoperability. Here are some examples of real projects to show the flexibility and potential of the birdhouse framework.

PAVICS
......

* PAVICS_: Platform for climate analysis and visualization by Ouranos_ and CRIM_, Canada.
* PAVICS-Hydro_ : Additional services for PAVICS_ allowing users to perform hydrological modeling and analysis.


.. gittoctree:: https://github.com/Ouranosinc/pavics-sdi.git

    docs/source/arch/backend.rst


.. gitinclude:: https://github.com/Ouranosinc/pavics-sdi.git docs/source/arch/backend.rst

DACCS
.....

* DACCS_: *Data Analytics for Canadian Climate Services* is a collaboration between the `University of Toronto`_,
  the Pacific Climate Impacts Consortium (PCIC_), the Computer Research Institute of Montréal (CRIM_), and Ouranos_.

  This project evolved from `PAVICS`_ developments, by extending Birdhouse_ services with multiple new capabilities,
  and providing an *Infrastructure as Code* (IaC) `birdhouse-deploy`_ definition allowing the customizable selection
  of server `components <https://birdhouse-deploy.readthedocs.io/en/latest/#birdhouse>`_.

COPERNICUS
..........

* CP4CDS: Climate Projects for the `Climate Data Store`_ (part of the European Union's `Copernicus Climate Change Service`_).

OGC-Testbeds
............

.. todo:: Add references to OGC testbed.

* OGC Testbed 13: Enhancement of scheduling services
* OGC Testbed 14: Enhancement of security


.. _A2C2: https://a2c2.lsce.ipsl.fr/
.. _PAVICS: https://ouranosinc.github.io/pavics-sdi/
.. _PAVICS-Hydro: https://medium.com/birdhouse-newsletter/web-processing-services-for-hydrological-modeling-7b5eb5c426ed
.. _PAVICS_architecture: https://ouranosinc.github.io/pavics-sdi/_sources/arch/backend.rst.txt
.. _PCIC: https://www.pacificclimate.org/
.. _DACCS: https://daccs.ca/
.. _University of Toronto: https://www.utoronto.ca/
.. _Ouranos: https://www.ouranos.ca/
.. _CRIM: https://www.crim.ca/en
.. _Climate Data Store: https://cds.climate.copernicus.eu/
.. _Copernicus Climate Change Service: https://climate.copernicus.eu/
