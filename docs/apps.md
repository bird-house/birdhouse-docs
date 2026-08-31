# Climate Services Application Packages

Here is a list of active software packages, applications and utilities to be used to spin off technical climate services information systems.
They are compliant with approved international standards to ensure technical interoperabillity.
Birds are services providing processes for specific thematic subjects.
For example to access climate data or to run a cyclone tracking tool.
The services are using pygeoapi from the GeoPython project.
Birdhouse provides tools (cockiecutter-template, birdy client, docker, ...) to make it easier to build, use, maintain, and deploy new thematic birds.

The sources of the software packages are centralised in the GitHub Organisation [Bird-House](https://github.com/bird-house).
Some applications are stored in different places due to the development history, funding mechanism, or intellectual property rights.

## **Testsuits**

| Name and Documentation  | Usage | Standard | Source |
| -------- | ------- | ------- | ------- |
| **nandu** | Nandu is a demo for ogcapi-process using pygeoapi (like the Emu for PyWPS) |  pygeoapi | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://nandu.readthedocs.io/en/latest/) <br> [![GitHub Nandu](https://img.shields.io/badge/GitHub-nandu-brightgreen.svg)](https://github.com/bird-house/nandu/) |
| **emu**  |  Demo and testing application for training purpose (like the Nandu for PyGeoAPI) | pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://emu.readthedocs.io/) <br> [![GitHub Emu](https://img.shields.io/badge/GitHub-emu-brightgreen.svg)](https://github.com/bird-house/emu) |
| **flyingpigon**  | Test-suite for experimenting on processes and data analytics |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://flyingpigeon.readthedocs.io) <br> [![GitHub Flyingpigeon](https://img.shields.io/badge/GitHub-flyingpigeon-brightgreen.svg)](https://github.com/bird-house/flyingpigeon) |

## **Utilities and Clients**

| Name and Documentation  | Usage | Source |
| -------- | ------- | ------- |
| **twitcher** | Security Proxy for WPS, WCS, WMS  | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](http://twitcher.readthedocs.io/) <br> [![GitHub twicher](https://img.shields.io/badge/GitHub-twitcher-brightgreen.svg)](https://github.com/bird-house/twitcher/)  |
| **cookiecutter-birdhouse** | Utility to create an OGC API Processes application package skeleton | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://cookiecutter-birdhouse.readthedocs.io) <br> [![GitHub twicher](https://img.shields.io/badge/GitHub-twitcher-brightgreen.svg)](https://github.com/bird-house/cookiecutter-birdhouse) |
| **birdy**  |   Python WPS client to call a serverside deployed application package  | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://birdy.readthedocs.io) <br> [![GitHub birdy](https://img.shields.io/badge/GitHub-birdy-brightgreen.svg)](https://birdy.readthedocs.io/en/latest/) |
| **Rooki**  |  The rooki Python package is a lightweight wrapper around the birdy client library for WPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://rooki.readthedocs.io/en/latest/) <br> [![GitHub Rooki](https://img.shields.io/badge/GitHub-birdy-brightgreen.svg)](https://github.com/roocs/rooki) |

## **Frontend - Graphical User Interphase**

| Name  | Usage | Source |
| -------- | ------- | ------- |
| **Phoenix** | Graphical User Interphase Frontend | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://pyramid-phoenix.readthedocs.io/en/latest/) <br> [![GitHub Phoenix](https://img.shields.io/badge/GitHub-phoenix-brightgreen.svg)](https://github.com/bird-house/pyramid-phoenix.git) |


## **Climate Services Application Packages**

| Name  | Usage | Standard | Source |
| -------- | ------- | ------- | ------- |
| **magpie** | Magpie is service for AuthN/AuthZ accessible via a REST API implemented with the Pyramid web framework | REST API  | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://pavics-magpie.readthedocs.io/en/latest/) <br> [![GitHub Magpie](https://img.shields.io/badge/GitHub-magpie-brightgreen.svg)](https://github.com/Ouranosinc/Magpie) |
| **weaver** | Execution Management Service that allows the execution of workflows chaining various applications and Web Processing Services inputs and outputs  |OGC-API-Processes | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://pavics-weaver.readthedocs.io/en/latest/) <br> [![GitHub Weaver](https://img.shields.io/badge/GitHub-weaver-brightgreen.svg)](https://github.com/crim-ca/weaver) |
| **finch** | application package for processing services to calculate climate indices |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://pavics-sdi.readthedocs.io/projects/finch) <br> [![GitHub Finch](https://img.shields.io/badge/GitHub-weaver-brightgreen.svg)](https://github.com/bird-house/finch) |
| **rooks**| Remote operations on climate simulations |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://rooki.readthedocs.io/en/latest/) <br> [![GitHub Weaver](https://img.shields.io/badge/GitHub-rooki-brightgreen.svg)](https://roocs.github.io/) |
| **raven** | Hydrological modeling and analytics | pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://pavics-sdi.readthedocs.io/projects/raven/en/latest/index.html) <br> [![GitHub Weaver](https://img.shields.io/badge/GitHub-raven-brightgreen.svg)](https://github.com/Ouranosinc/raven.git) |
| **duck** | AI enhanced process to fill in missing values |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://clint-duck.readthedocs.io/en/latest/) <br> [![GitHub Weaver](https://img.shields.io/badge/GitHub-weaver-brightgreen.svg)](https://github.com/climateintelligence/duck) |
| **hawk** | Causal analysis for climate data or, in general, for time-series | pyWPS| [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://clint-hawk.readthedocs.io/en/latest/) <br> [![GitHub Weaver](https://img.shields.io/badge/GitHub-hawk-brightgreen.svg)](https://github.com/climateintelligence/hawk) |
| **albatross** | Climate resilience application package for drought assessment |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://clint-albatross.readthedocs.io/en/latest/) <br> [![GitHub albatross](https://img.shields.io/badge/GitHub-albatross-brightgreen.svg)](https://github.com/climateintelligence/albatross)|
| **shearwater** | Perform detection and forecast of tropical-cyclone activities |  pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://shearwater.readthedocs.io/en/latest/) <br> [![GitHub Shearwater](https://img.shields.io/badge/GitHub-shearwater-brightgreen.svg)](https://github.com/climateintelligence/shearwater)|
| **owl** | Heatwave magnitude index and warm nights | pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://clint-owl.readthedocs.io/en/latest/) <br> [![GitHub Owl](https://img.shields.io/badge/GitHub-owl-brightgreen.svg)](https://github.com/climateintelligence/owl)|
| **hummingbird** | data compliance checker | pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](http://birdhouse-hummingbird.readthedocs.io/) <br> [![GitHub Hummingbird](https://img.shields.io/badge/GitHub-hummingbird-brightgreen.svg)](https://github.com/bird-house/hummingbird.git)|
| **goldfinch** | filtering and extraction of MIDAS data | pyWPS |[![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://github.com/cedadev/goldfinch) <br> [![GitHub Goldfinch](https://img.shields.io/badge/GitHub-weaver-brightgreen.svg)](https://github.com/cedadev/goldfinch) |
| **pelican** | WPS supporting ESGF compute API | pyWPS | [![Documentation Status](https://img.shields.io/badge/docs-latest-blue.svg)](https://birdhouse-pelican.readthedocs.io/en/latest/) <br> [![GitHub Pelican](https://img.shields.io/badge/GitHub-pelican-brightgreen.svg)](https://github.com/bird-house/pelican) |

<!-- | [dipper](https://clint-dipper.readthedocs.io/en/latest/) | ------- | [Dipper GitHub Repository](https://github.com/climateintelligence/dipper) | -->
