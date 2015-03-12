.. _faq:

==========================
Frequently Asked Questions
==========================

.. contents::
   :local:
   :depth: 2
   :backlinks: none

General Questions
=================

*What is "Birdhouse"?*
----------------------

*Birdhouse* is collection of Python packages to make the usage of Web Processing Services (WPS) easy.
The available packages are used in the climate science community.

*What is "WPS"?*
----------------

The very short answer: 

WPS is the acronym for Web Processing Service.

The sligthly longer answer:

So, let's say you have a function (maybe written in Python) which might calculate the "summer days in finland since 1990". Then this function has probably input parameters (region, from-date, to-date, NetCDF files, ...) and an output (or even more ...) which might be just a interger number or a text document or even a diagram. Now, you would like to provide this function as a web service, so that other people can call it with just a simpel URL like http://myhost/wps/identifier=summer_days&region=finland ... ok ... then you should have a deeper look at this WPS thing  ... 

Getting Help
============ 


