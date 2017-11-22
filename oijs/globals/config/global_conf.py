#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: global.config.global_conf


"""
module oijs.globals.config.global_conf
"""


import sys
import os
from . import conf_helper
from ..exception.exception import oijs_exception


config = {}   # pylint: disable=C0103


def load_conf():
    """
    load_conf
    """

    default_conf = conf_helper.load_conf(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'default_conf/oijs_global_conf.yml'
        )
    )
    custom_conf = conf_helper.load_conf(
        os.path.expanduser('~/.oijs/config.yml'))
    global config   # pylint: disable=W0603, C0103
    try:
        config = conf_helper.join_conf(default_conf, custom_conf)
    except oijs_exception as err:
        print(err.error(), file=sys.stderr)
        exit(1)
