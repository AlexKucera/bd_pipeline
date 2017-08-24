#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

"""
Global Variables

Will try to find its own path and use the hardcoded path if it cannot find the global config file on its own.
"""

import bd_globals
import os

# Config

CONFIG_PATH = '/Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/bd_pipeline/'
CONFIG_NAME = 'global_config.json'

# Automated Stuff.  No Touchy!

globals_config_path = os.path.dirname(bd_globals.__file__) + os.sep + CONFIG_NAME

if os.path.exists(globals_config_path):
    CONFIG_PATH = globals_config_path
else:
    CONFIG_PATH += CONFIG_NAME


