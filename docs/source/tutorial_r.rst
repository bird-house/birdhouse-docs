Pywps with R
============
The following shows how you can wrap R software with pyWPS

.. _rpy2:

Rpy2
....
There’s several R-to-python Python libraries but `Rpy2 <https://rpy2.github.io/doc/latest/html/index.html>`_ is probably the most well documented and most frequently used. Any R library can be accessed, as long as it is installed, with :code:`importr([package-name])`. Since R :code:`base` and :code:`utils` are installed with :code:`rpy2` you can import them:

.. code-block:: Python
   
   from rpy2.robjects.packages import importr
   base = importr("base")
   utils = importr("utils")
   
Then you can use functions from that package with :code:`package.function_name()`. If the R function name has a period '.' it is replaced with an underscore in python.
 
.. code-block:: Python

   base.all(True)
   base.all_equal("hello","world")
 
You can execute any regular R code as a string passed to :code:`robjects.r()`

.. code-block:: Python

   from rpy2 import robjects
   robjects.r("c(1,2,3)")d
   
Install another package with Rpy2 and use the functions form that package...

.. code-block:: Python

   utils.install_packages("climdex.pcic")
   climdex_pcic = importr("climdex.pcic")
   climdex.climdex_gsl(climdexInput, gsl_mode)
   
.. _input:

Input
.....
  
If an R object input is needed you can store the object in a RDS or Rdata file and read as a :code:`ComplexInput` with :code:`format`:

.. code-block:: Python

   from pywps import ComplexInput, Format
   
   ComplexInput(
      "r_file",
      "R data file",
      supported_formats=[Format("application/x-gzip", encoding="base64")],
   )
  
