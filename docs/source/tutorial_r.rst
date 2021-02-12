Pywps with R
============
The following shows how you can wrap R software with pyWPS.

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
There’s several R-to-python Python libraries but `Rpy2 <https://rpy2.github.io/doc/latest/html/index.html>`_ is probably the most well documented and most frequently used. Any R library can be accessed, as long as it is installed, with :code:`importr([package-name])`. Since R :code:`base` and :code:`utils` are installed with :code:`rpy2` you can import them:

.. code-block:: Python
   
   from rpy2.robjects.packages import importr
   base = importr("base")
   utils = importr("utils")
   
Then you can use functions from that package with :code:`package.function_name()`. If the R function name has a period '.' it is replaced with an underscore '_' in python.
 
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
  
.. _dep:

Installing Dependencies
.......................
With a simple Rscript you can install dependencies similarly to installing Python dependencies with :code:`requirements.txt`.

**install_pkgs.R:**

.. code-block:: R

   # Usage:
   # Rscript install_pgks.R r_requirements.txt
   # r_requirements delimited by '==' as in python requirements.txt

   # Create user library
   dir.create(Sys.getenv('R_LIBS_USER'), recursive = TRUE);
   .libPaths(Sys.getenv('R_LIBS_USER'));

   # Install devtools and its dependencies
   install.packages('devtools', dependencies=TRUE);

   # Install packages from requirements list
   args <- commandArgs(trailingOnly = TRUE)
   req_filename <- args[1]
   requirements_file <- file(req_filename,open="r")
   data <-readLines(requirements_file)
   for (i in 1:length(data)){
       pkg_ver_pair <- unlist(stringr::str_split(data[i], "=="))
       pkg<-pkg_ver_pair[1]
       ver<-pkg_ver_pair[2]
       if (is.na(ver)){
           devtools::install_version(pkg)
       } else {
           devtools::install_version(pkg, version = ver);
       }
   }
   close(requirements_file)
   
Which Reads from a file similar to :code:`requirements.txt` for Python dependencies:

**r_requirements.txt:**

.. code-block::
   
   PCICt==0.5.4.1
   climdex.pcic==1.1.11


.. _docker:

Dockerfile
............
To install :code:`Rpy2`, R needs to be installed already. A good base image for R is `rocker/r-ver <https://hub.docker.com/r/rocker/r-ver>`_ and you can install Python on top of it. Check out the `pcic/quail Dockerfile <https://github.com/pacificclimate/quail/blob/master/Dockerfile>`_ as an example.
