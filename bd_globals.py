#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

The idea when I am done is for this to be the central repository of all things pipeline.

Release Notes:

V0.1 Initial Release


(\d+)(?:[,-](\d+))?(?:[,xX:](\d+))? # Catches simple positive number combinations

(\d+)(?:\s)?(?:[,-](?:\s)?(\d+))?(?:\s)?(?:[,xX:](?:\s)?(\d+))? # Catches most positive number combinations.

(-?\d+)(?:\s)?(?:[,-](?:\s)?(-?\d+))?(?:\s)?(?:[,xX:](?:\s)?(-?\d+))? # Catches most negative number combinations.

http://sarge.readthedocs.io/en/latest/overview.html#what-is-sarge-for

http://amoffat.github.io/sh/index.html

http://plumbum.readthedocs.io/en/latest/


"""
import os
import json

import re

from vars import *


# FUNCTIONS -----------------------------------------------
class QueryDict(dict):
    """
    Creates a Dictionary that is browseable by path.

    Example:

        query_dict = {'key': {'subkey': 'value'}}

        print query_dict['key/subkey']

    """
    def __getitem__(self, key_string):
        current = self
        try:
            for key in key_string.split('/'):
                current = dict.__getitem__(current, key)
            return current
        except (TypeError, KeyError):
            return None


def walk_up(bottom):
    """
    mimic os.walk, but walk 'up'
    instead of down the directory tree

    os.walk is an awesome generator.
    However, I needed the same functionality, only I wanted to walk 'up' the directory tree.
    This allows searching for files in directories directly above a given directory.

    via: https://gist.github.com/zdavkeos/1098474
    """

    bottom = os.path.realpath(bottom)
    if os.path.isfile(bottom):
        bottom = os.path.dirname(bottom)

    # get files in current dir
    try:
        names = os.listdir(bottom)
    except Exception as e:
        print(e)
        return

    dirs, nondirs = [], []
    for name in names:
        if os.path.isdir(os.path.join(bottom, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    yield bottom, dirs, nondirs

    new_path = os.path.realpath(os.path.join(bottom, '..'))

    # see if we are at the top
    if new_path == bottom:
        return

    for x in walk_up(new_path):
        yield x


def find_project(filepath):

    """
    Tries to find the project folder for any given file based on the global pipeline config.
    :param filepath:
    :return:
        None if no project was found
        project (dict) containing project directory, project name and client name if a project was found.
    """

    regex_string = "({0})([^/]+)/([^/]+)".format(bdconfig()['projects dir'])
    regex = re.compile(regex_string)
    match = re.match(regex, filepath)

    if match is not None:
        client = match.group(2)
        project = match.group(3)
        project_dir = match.group()

        return {'project_dir': project_dir, 'client': client, 'project': project}

    else:

        return None


def find_shot_version(filepath):
    """
        Tries to find the version number for any given file based on the global pipeline config.
        :param filepath:
        :return:
            None if no project was found
            project (dict) containing project directory, project name and client name if a project was found.
        """

    regex_string = '.*(([a-zA-Z0-9]{{{}}})_([a-zA-Z0-9]{{{}}})_.*)v(\d{{{}}})(.*)(\.[a-zA-Z].+)'.format(
        projectconfig(filepath)['numbering/sequence digits'],
        projectconfig(filepath)['numbering/shot digits'],
        projectconfig(filepath)['numbering/version digits']
    )

    regex = re.compile(regex_string)
    match = re.match(regex, filepath)
    if match:
        shotname = match.group(1).rstrip('_ -')
        return {'sequence': match.group(2), 'shot': match.group(3), 'version': match.group(4), 'shotname': shotname}


def bdconfig():
    """
    Returns a dictionary with found global pipeline data based on the global project definitions.

    :return: babvars (dict)
    """

    with open(CONFIG_PATH) as json_data:
        bab_vars = QueryDict(json.load(json_data))

    bab_vars['projects dir'] = "{drive}{sep}{projects}{sep}".format(drive=bab_vars['project drive'],
                                                                   projects=bab_vars['projects location'],
                                                                   sep=os.sep)

    return bab_vars


def projectconfig(filepath):
    """
    Returns a dictionary with found project data based on the global project definitions.
    If a valid project path is found it tries to reads it's project config. If none exists the global config is used.
    :param filepath:
    :return: projectvars (dict)
    """
    project = find_project(filepath)
    bdconfigs = bdconfig()

    if project is None:
        project_config = "{}{}".format(CONFIG_PATH, bdconfigs['project config name'])

    else:
        project_config = "{}{}{}".format(project['project_dir'], os.sep, bdconfigs['project config name'])

    with open(project_config) as json_data:
        project_vars = QueryDict(json.load(json_data))

    return project_vars

# END FUNCTIONS -----------------------------------------------
