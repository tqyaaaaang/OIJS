#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.config.global_conf


"""
module oijs.globals.config.global_conf
"""


import sys
import os
from oijs.globals.config import conf_helper
from oijs.globals.exception.exception import oijs_exception

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources


config = {}   # pylint: disable=C0103


def load_conf():
    """
    load_conf
    """

    with pkg_resources.open_text(
        'oijs.globals.config.default_conf',
        'oijs_global_conf.yml'
        ) as DEFAULT_CONF:
        default_conf = conf_helper.load_conf(DEFAULT_CONF)
    with open(os.path.expanduser('~/.oijs/config.yml')) as CUSTOM_CONF:
        custom_conf = conf_helper.load_conf(CUSTOM_CONF)
    global config   # pylint: disable=W0603, C0103
    try:
        config = conf_helper.join_conf(default_conf, custom_conf)
    except oijs_exception as err:
        print(err.error(), file=sys.stderr)
        exit(1)
