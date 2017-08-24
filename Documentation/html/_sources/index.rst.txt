.. BabylonDreams Kit documentation master file, created by
   sphinx-quickstart on Wed Feb 15 14:21:00 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to BabylonDreams Pipeline's documentation!
===========================================================

.. toctree::
    :maxdepth: 4
    :caption: Contents:

    modules

The BabylonDreams Pipeline contains scripts, configs and functions essential to our pipeline.

It is pretty much hard coded for our internal pipeline at the moment and very much in flux. But it may contain a few useful functions or ways of doing things. Feel free to adapt or improve upon my work.

Disclaimer
===========

I am not a trained programmer and I usually don't have much time to code. So be prepared for ugly code, quick hacks and stuff that is half finished. You have been warned.

Summary
=======

This module is meant as a pipeline wide glue between applicaitons. It allows querying project information such as a project's name or a file's version number by simply providing a file path.

There are at the moment four main functions defined:

	* bdconfig
	* projectconfig
	* find_project
	* find_shot_version


bdconfig
--------

Usage: `bdconfig()`

Looks at the global `global_config.json` that lives in this modules directory. It contains facility wide global settings like the path to projects and other global paths.

projectconfig
-------------

Usage: `projectconfig(filepath)`

First it tries to find a file called `project_config.json` inside a provided path's project structure. If it is unable to find such a file (or project structure) it will resort to reading the default `project_config.json`that is in this module's directory. This function returns project specific details such as frame rates, project name or which folders are to be found where inside the project folder.


find_project
------------

Usage: `find_project(filepath)`

Give it a file path and it will find the project this path belongs to.

It will return a dictionary containing project directory, project name and client name if a project was found.

find_shot_version
-----------------

Usage: `find_shot_version(filepath)`

Tries to find the version number for any given file based on the project config.

Returns a dictionary with the sequence, shot, version number and shot/file name.
	
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`