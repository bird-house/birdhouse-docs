.. _birdhouse_ecosystem:

Set up a birdhouse ecosystem server
===================================

If you are already familliar with installing single standalone WPS ( follow the installation guides in the documentations of e.g. emu ), than you are ready to set up a birdhouse containing flyingpigeon (providing scientific anlyses methods), malleefowl ( to search and fetch data ) and the pheonix ( a graphic interphase for a web browser ). 

general remarques:  
..................

Check the ref:`requirements`_ of your system!
The installation is done as **normal user**, root right are not required. 


clone the repositories from gitHub: 
...................................

It is recommended to collect the repositories in a seperate folder ( e.g. birdhouse but can has a name of your choice ):

mkdir birdhouse  
cd birdhouse


* **fetch the source code:** 

git clone https://github.com/bird-house/flyingpigeon.git

git clone https://github.com/bird-house/pyramid-phoenix.git

git clone https://github.com/bird-house/malleefowl.git

* **pheonix password**

To be able to log into the Phoenix GUI once the services are running, it is necessary to generate a password:
  walk into the pyramid-phoenix folder and run: 

make passwd

this will automatically write a password hash into pyramid-phoenix/custom.cfg


* **installation**

You can run the installation with default settings.
  It will create an anaconda environment into your HOME direcory and deploy all required software dependecies there. 
  *read the ''changing the default configuration' frist if you like to change the defaults.*

In **all** of the tree folders (malleefowl, flyingpigeon and pyramid-phoenix) run:

make install

This installation will take some minutes. Fetching all dependencies and installing them into seperate conda environments.
  With the default settings the installation is creating the following folders: 

*~/anaconda/*
  containing general software required by anaconda

*~/.conda/envs/*
  containing the seperat environments of the birds for their specific software dependencies

*~/birdhouse/var/*
  the local cache for fetched input files, output files and logs. This folder is growing (while fetching files and storing job outputs) under productive usage of birdhouse.

* **start the services**

in **one** of the birds run 

make start 
  or 
  make restart

and to check if the services are running run: 
  make status

* **launching the Phoenix GUI**

If the services are running you can launch the GUI in a common web browser. Per default phoenix is set to port 8081

firefox http://phoenix:8081
  or 
  firefox https://localhost:8443/

Now you can log in ( upper right corner ) with your in the beginning created Phoenix password. 
Phoenix is just a graphical interphase with not more functions than looking nice ;-). 

* **register a service in the GUI**

Your first administer step is to register flyingpigeon as a service. For that log in with your phoenix password. 
In the upper right corner is a tool symbol to open the 'settings'. Click on 'Services' and the 'Register a Service'. 

flyingpigeon is per default at port 8093. 

the appropriate url is: 

http://localhost:8093/wps

Provide service title and name as you like: 
  Service Title: Flyingpigeon
  Service Name: flyingpigeon

check 'Service Type' : 'Web Processing Service' (default) and register. 

Optional you can check 'Public access?', to allow unregistered users launching jobs. (**NOT recommendet**)


* **launching a job**

Now your birdhouse ecosysem is set up. The also installed malleefowl is already running in the background and will do a lot of work silently. Ther is **no need to register malleefowl** manually!

Launching a job can be performed over processes or the wizard. To get familliar with the processes provided by each of the birds, read the approriate documentation for each of the services listed in the `overview: <http://birdhouse.readthedocs.io/en/latest/index.html>`_ 

* **changing the default configuration:**

default configuration can be changed by creating a Makefile.config file. There is an example provided to be used:  

cp Makefile.config.example Makefile.config
  and set the appropriate path. You have to **do this in all** bird repositories. 

Further you might change the hostname (to provide your service to the outside), ESGF-node connection, the port or the log-level for more/less information in the adminiser logfiles. 
here is an example pyramid-phoenix/custom.cfg:

[settings]
hostname = birdhouse-lsce.extra.cea.fr
http-port = 8081
https-port = 8443
log-level = DEBUG 
# run 'make passwd' and to generate password hash
phoenix-password = sha256:513....
# generate secret
# python -c "import os; print(''.join('%02x' % ord(x) for x in os.urandom(16)))"
phoenix-secret = d5e8417....30
#esgf-search-url = https://esgf-node.ipsl.upmc.fr/esg-search 
esgf-search-url = https://esgf-data.dkrz.de/esg-search
wps-url = http://birdhouse-lsce.extra.cea.fr:8091/wps
# swift access
swift-auth-url = http://birdhouse-lsce.extra.cea.fr/auth/v1.0
swift-auth-version = 1
# register at github: https://github.com/settings/applications/new 
github-consumer-key = 86......02
github-consumer-secret = 2c.........6d4

* **Administration HELP:**

In case of questions or trouble shooting, feel welcome to join the birdhouse chat and get into contact with the developers directly: 

`Birdhouse-Chatroom <https://gitter.im/bird-house/birdhouse>`_








