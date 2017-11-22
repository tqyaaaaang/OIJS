#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.data.global_data


"""
module oijs.globals.data.global_data
"""


import sys
import os


def load_data():
    """
    load_data
    """

    global current_dir   # pylint: disable=W0603, C0103
    current_dir = os.path.abspath('{}/..'.format(sys.path[0]))


current_dir = ''   # pylint: disable=C0103

run_mode = None   # pylint: disable=C0103
