PyWPS with R
============
The following shows how you can wrap R software with PyWPS.

.. _examples:

Examples of R Birds
...........................
* `pcic/quail <https://github.com/pacificclimate/quail>`_

  * `wps_climdex_gsl.py <https://github.com/pacificclimate/quail/blob/master/quail/processes/wps_climdex_gsl.py>`_
* `pcic/chickadee <https://github.com/pacificclimate/chickadee>`_

  * `wps_BCCAQ.py <https://github.com/pacificclimate/chickadee/blob/master/chickadee/processes/wps_BCCAQ.py>`_ 

.. _rpy2:

Rpy2
....
There’s several R-to-python Python libraries but `Rpy2 <https://rpy2.github.io/doc/latest/html/index.html>`_ is probably the most well documented and most frequently used. As long as it is installed, a R library can be accessed with :code:`importr([package-name])`. Since R :code:`base` and :code:`utils` are installed with :code:`rpy2` you can import them:

.. code-block:: Python
   
   from rpy2.robjects.packages import importr
   base = importr("base")
   utils = importr("utils")
   
Then you can use functions from that package with :code:`package.function_name()`. If the R function name has a period :code:`.` it is replaced with an underscore :code:`_` in python.
 
.. code-block:: Python

   base.all(True)
   base.all_equal("hello","world") # all.equal() in R
 
You can execute any regular R code as a string passed to :code:`robjects.r()`

.. code-block:: Python

   from rpy2 import robjects
   count = robjects.r("c(1,2,3)")
   robjects.r("all(T)")
   
You can also access R functions with the syntax :code:`robjects.r["function.name"]` if you want to avoid the import step.

.. code-block:: Python

   robjects.r["save"](count, file=output_path)
   
Install another package with Rpy2 and use the functions form that package...

.. code-block:: Python

   utils.install_packages("climdex.pcic")
   climdex_pcic = importr("climdex.pcic")
   climdex_pcic.climdex_gsl(climdexInput, gsl_mode)
   
.. _io:

I/O
.....
  
Rpy2 handles R-to-python conversions of `LITERAL_DATA_TYPES <https://pywps.readthedocs.io/en/latest/api.html#pywps.inout.literaltypes.LITERAL_DATA_TYPES>`_, but objects of other types may need to be stored in a RDS or Rdata file. RDS files and Rdata files are indistinguishable by mime type when read to the server so their handling has to be done elsewhere in the processes. You can see how it's handled in PCIC's `quail <https://github.com/pacificclimate/quail/blob/6f89a3f2d2d7effb2ee22bb7e6a8ae1a74c6e6cc/quail/utils.py#L91>`_. Read the file as a :code:`ComplexInput` with :code:`format`:

.. code-block:: Python

   from pywps import ComplexInput, Format
   
   ComplexInput(
      "r_file",
      "R data file",
      supported_formats=[Format("application/x-gzip", encoding="base64")],
   )
   
... And if your output is an R object you can save that object to an RDS or Rdata file and return it with :code:`ComplexOutput`:

.. code-block:: Python

   from pywps import ComplexOutput
   
   ComplexOutput(
     "r_output",
     "R output file",
     supported_formats=[Format("application/x-gzip", extension=".rda", encoding="base64")],
   )
  
.. _dep:

Installing Dependencies
.......................
You can write a simple script in :code:`R`, :code:`bash`, or :code:`Python` to automate installation of R package dependencies. :code:`devtools::install_version()` is used to pin versions in PCIC's :code:`quail` and :code:`chickadee`. You can take a look at the R script `here <https://github.com/pacificclimate/quail/blob/cd60aabcfdcae249921541f6e969de26a2695127/install_pkgs.R>`_. 
   
The script reads from a file similar to :code:`requirements.txt` for Python dependencies:

**r_requirements.txt:**

.. code-block::
   
   PCICt==0.5.4.1
   climdex.pcic==1.1.11


.. _docker:

Dockerfile
............
To install :code:`Rpy2`, R needs to be installed already. A good base image for R is `rocker/r-ver <https://hub.docker.com/r/rocker/r-ver>`_ and you can install Python on top of it. Check out the `pcic/quail Dockerfile <https://github.com/pacificclimate/quail/blob/master/Dockerfile>`_ as an example.
