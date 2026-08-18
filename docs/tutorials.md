# **Tutorials**

Here you can find a collection of tutorials, provided by the several contributing initiatives.If you see a need of changing, updating or adding to this documentation, here is an *How To DO* on how to [contribute to this documentation](sections/tutorial_docs.md)

## Calling a **OGC API Processes service** with python

To call a OGC API Processes service within a python code here is a small code snipped. Birdhouse provides the testsuite [*nandu*](https://nandu.readthedocs.io/en/latest/) complient to the OGCAPI Processes.

``` python
from owslib.ogcapi.processes import Processes
nandu = Processes(url="http://localhost:5000")
nandu.api()
```
> Clients and services are currently under development and will be provided by the upcomming releases.

## Calling a **WPS service** with python
To call a WPS service within a python code, [birdy](https://github.com/bird-house/birdy.git) is provided as a client to do this job.

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

> For further tutorials and information on pyWPS please have a look on [WPS Tutorials](sections/tutorial_wps.md)

## Calculating Climate Indices
**Finch** is providing services to calculate climate indices widely used in climate change adaptation planing processes. Have a look on the examples of the [finch documentation](https://pavics-sdi.readthedocs.io/projects/finch/en/latest/notebooks/index.html), where executable *jupyter notebooks* are provided on how to calculate climate indices.

## Running hydrological models
**raven** is providing hydrological models for e.g. hydro-power controlling and sustainable planing. Have a look on the examples of the raven documentation: [Hydrological Model](https://pavics-raven.readthedocs.io/en/latest/notebooks/index.html)

## Artificial Intelligence enhanced climate servies
Extreme event detection and prediction for cyclon activity, droughts, heatwaves or floods, using artificial intelligence methodes has been developed in the CLINT Project. Juypter Notebooks on how to handle and run this proceses are proviced in the [Climate Intelligence CLINT Project](https://github.com/climateintelligence/CLINT-tutorials)

<!--
docs/source/examples.rst
tutorial_basic tutorial_pywps tutorial_wps tutorial_server tutorial_r
 -->


