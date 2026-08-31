# **Tutorials**

On this page are a set of tutorials, provided by the many contributing initiatives.
If you see something here that requires updating or would like to add to this documentation, please consult the page on [contributing to this documentation](sections/tutorial_docs.md).

## Calling a **OGC API Processes service** with Python

Below is an example of how to call a OGC API Process services within Python code.
Birdhouse provides the test suite [*nandu*](https://nandu.readthedocs.io/en/latest/), compliant with the OGC API Processes.

``` python
from owslib.ogcapi.processes import Processes

nandu = Processes(url="http://localhost:5000")
nandu.api()
```
> Clients and services are currently under development and will be provided by the upcoming releases.

## Calling a **WPS service** with Python
To call a WPS service from Python, [birdy](https://github.com/bird-house/birdy.git) is provided as an interaction client.

``` python
from birdy import WPSClient

emu = WPSClient(url="http://localhost:5000/wps")
emu_i = WPSClient(url="http://localhost:5000/wps", progress=True)
emu.hello(name="Birdy").get()[0]
# Run a long running process
result = emu_i.sleep(delay="1.0")
result.get()[0]
```
> Further tutorials on how to run the birdy client can be found at [birdy documentation](https://birdy.readthedocs.io/en/latest/)

> For more information on PyWPS, please have a look on [WPS Tutorials](sections/tutorial_wps.md)

## Calculating Climate Indices
**Finch** is providing services to calculate climate indices widely used in climate change adaptation planing processes. Have a look on the examples of the [finch documentation](https://pavics-sdi.readthedocs.io/projects/finch/en/latest/notebooks/index.html), where executable *jupyter notebooks* are provided on how to calculate climate indices.

## Running hydrological models
**raven** is providing hydrological models for e.g. hydro-power controlling and sustainable planing. Have a look on the examples of the raven documentation: [Hydrological Model](https://pavics-raven.readthedocs.io/en/latest/notebooks/index.html)

## Artificial Intelligence enhanced climate services
Extreme event detection and prediction methods for cyclone activity, droughts, heatwaves or floods, using artificial intelligence have been developed in the CLINT Project. Juypter Notebooks on how to handle and run these processes are provided in the [Climate Intelligence CLINT Project](https://github.com/climateintelligence/CLINT-tutorials)

<!--
docs/source/examples.rst
tutorial_basic tutorial_pywps tutorial_wps tutorial_server tutorial_r
 -->
