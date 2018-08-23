Example
-------

.. todo:: This example with Flyingpigeon is outdated.

Data production
...............

WPS is designed to reduce data transport and enables data processing close to the data archive.
Nevertheless, files are stored within birdhouse in a structured way.
For designing a WPS process or process chain, the location of input, output and temporary files are illustrated as follows:

.. image:: _images/filelocations.png


Resources, which are already on the local disc system (output by other processes or as locally stored data archives),
are linked into the cache simply with a soft link to avoid data transport and disc space usage.

The locations are defined as follows:

* **Resources:** Any kind of accessable data such as ESGF, thredd server or files stored on the server-side disc system.

* **Cache:** ``~/birdhouse/var/lib/pywps/cache/`` The cache is for external data which are not located on the server side. The files of the cache are separated by the birds performing the data fetch and keep the folder structure of the original data archive. Once a file is already in the cache, the data will not be refetched if a second request is made. The cache can be seen as a local data archive. Under productive usage of birdhouse, this folder is growing, since all requested external data are stored here.

* **Working directory:** ``~/birdhouse/var/lib/pywps/tmp/`` Each process is running in a temporary folder (= working directory) which is removed after the process is successfully executed. Like the cache, the working directories are separated by birds. Resource files are linked into the directory.

* **Output files:** ``~/birdhouse/var/lib/pywps/outputs/`` The output files are also stored in output folders separated by the birds producing the files. In the case of flyingpigeon, you can get the paths with:

.. code-block:: python

   from flyingpigeon import config

   output_path = config.output_path()        # returns the output folder path
   outputUrl_path = config.outputUrl_path()  # returns the URL address of the output folder


And in some special cases, static files are used (e.g. html files to provide general information).
These files are located in the repository. In the case of flyingpigeon, they are located at: ``./flyingpigeon/flyingpigeon/static/``

and copied during the installation (or update) to: ``~/birdhouse/var/www/``

.. _processdesign:

Designing a process
-------------------

For designing a process it is necessary to know some basic concepts about how data are produced in birdhouse.
The following are some basic explanations to help in developing appropriate processes to provide a
scientific method as a service. The word **process** is used in the same sense as in the
OGC standard: *for any algorithm, calculation or model that either generates new data or transforms some input data into output data*,
and can be illustrated as follows:

.. image:: _images/process_schema_1.png

The specific nature of web processing services is that processes can be described in a standardised way (see:
:ref:`writing_WPS_process`). In the flyingpigeon repository, the process descriptions are located in::

    ./flyingpigeon/flyingpigeon/processes

As part of the process description there is an **execute** function:

.. code-block:: python

   def execute(self):
       # here starts the actual data processing
       import pythonlib
       from flyingpigeon import aflyingpigeonlib as afl

       result = afl.nicefunction(indata, parameter1=argument1, parameter2=argument2)

       self.output.setValue( result )


It is a recommended practice to separate the functions (the actual data processing) from the process description.
This creates modularity and enables multiple usage of functions when designing several processes.
The modules in flyingpigeon are located here::

    ./flyingpigeon/flyingpigeon

Generally, the execution of a process contains several processing steps, where temporary files and memory values are generated.
Birdhouse runs each job in a separate folder, by default situated in::

    ~/birdhouse/var/lib/pywps/tmp/

This tmp folder is removed after job is successfully executed. To reuse temporary files, it is necessary
to declare them as output files. Furthermore, during execution, there are steps which are necessary
to be successfully performed and a result is called back. If this particular step fails, the whole process should exit with an appropriate error message, while in other cases it is not relevent for producing the final result. The following image shows a theoretical chain of functions:

.. image:: _images/module_chain.png


In practice, the functions should be encapsulated in **try** and **except** calls and appropriate information
given to the log file or shown as a status message:

.. code-block:: python
   :linenos:

   from pywps.Process import WPSProcess
   import logging
   logger = logging.getLogger(__name__)

   # set a status message
   self.status.set('execution started at : %s ' % dt.now(),5)

   try:
       self.status.set('the process is doing something : %s '  % dt.now(),10)
       result = 42
       logger.info('found the answer of life')
   except:
       msg = 'This failed but is obligatory for the output. The process stops now!'
       logger.error(msg)
       raise Exception(msg)

   try:
       self.status.set('the process is doing something else : %s '  % dt.now(),20)
       interesting = True
       # or generate a temporary file
       logger.info(' Thanks for reading the guidelines ')
   except:
       msg = 'This failed but is not obligatory for the output. The process will continue.'
       logger.debug(msg)

   try:
       self.status.set('the process is doing something else : %s '  % dt.now(),20)
       interesting = True
       # or generate a temporary file
       logger.info(' Take your time to understand enverything ')
   except:
       msg = 'This failed. The process will continue but writes out the reason of the failture'
       logger.exception(msg)


   try:
       self.status.set('the process is doing something else : %s '  % dt.now(),20)
       interesting = True
       # or generate a temporary file
       logger.info(' This is the right way to do it  ')
   except:
       msg = 'Here comes a warning: Are you sure this is the right way to do it??'
       logger.warn(msg)


The log file then looks like::

  tail -f  ~/birdhouse/var/log/pywps/flyingpigeon.log

  PyWPS [2016-09-14 11:49:13,819] INFO: Start ocgis module call function
  PyWPS [2016-09-14 11:49:13,820] INFO: Execute ocgis module call function
  PyWPS [2016-09-14 11:49:13,828] DEBUG: input has Lambert_Conformal projection and can not subsetted with geom
  PyWPS [2016-09-14 11:49:13,828] DEBUG: failed for point ['2.356138', ' 48.846450'] Validation failed on the parameter "uri" with the message: Cannot be None
  PyWPS [2016-09-14 11:49:13,993] INFO: Start ocgis module call function
  PyWPS [2016-09-14 11:49:13,994] INFO: Execute ocgis module call function
  PyWPS [2016-09-14 11:49:14,029] INFO: OcgOperations set
  PyWPS [2016-09-14 11:49:14,349] INFO: tas as variable dedected
  PyWPS [2016-09-14 11:49:14,349] INFO: data_mb  = 0.0417938232422 ; memory_limit = 1660.33984375
  PyWPS [2016-09-14 11:49:14,349] INFO: ocgis module call as ops.execute()
  PyWPS [2016-09-14 11:49:16,648] INFO: Succeeded with ocgis module call function

Logging information is written to the logfile depending on the 'log-level' settings in ~/custom.cfg

Another point to think about when designing a process is the possibility of chaining processes together.
The result of a process can be a final result or be used as an input for another process.
Chaining processes is a common practice but depends on the user you are designing the service for.
Technically, for the development of WPS process chaining, here are a few summary points:

*    the functional code should be modular and provide an interface/method for each single task
*    provide a wps process for each task
*    wps processes can be chained, manually or programmatically, to run a complete workflow
*    wps chaining can be done manually, with workflow tools, direct wps chaining or with code scripts
*    a complete workflow chain could also be started by a wps process.

.. image:: _images/wps_chain.png

In birdhouse, restflow and dispel4py are integrated, and WPS chaining is used in the wizard of phoenix.
This WPS chain fetches data and runs a process (selected by the user) with the
fetched data : http://pyramid-phoenix.readthedocs.io/en/latest/user_guide.html#wizard


Here is a tutorial to follow: :ref:`chaining_WPS`.

or:

http://birdhouse.readthedocs.io/en/latest/appendix.html#scientific-workflow-tools
