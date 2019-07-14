#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.config.conf_helper


"""
module oijs.globals.config.conf_helper
"""


import os
import shutil
import yaml

from oijs.globals.data import global_data
from oijs.globals.exceptions.exception import OIJSException
from oijs import utils


def load_conf(curfile):
    """
    load_conf
    """

    config = {}
    config = yaml.load(curfile, Loader=yaml.FullLoader)
    return config


def join_conf(default_conf, custom_conf, current_config=''):   # pylint: disable=R0912
    """
    join_conf
    """

    if (isinstance(default_conf, dict)) and not isinstance(custom_conf, dict):
        if custom_conf is None:
            return default_conf
        raise OIJSException(
            'FATAL ERROR : {} should be a map. An item was found.'.format(
                current_config))

    cur_conf = default_conf

    for cur in custom_conf:   # pylint: disable=R1702
        if cur in cur_conf:
            if isinstance(cur_conf[cur], dict):
                join_conf(cur_conf[cur], custom_conf[cur],
                          current_config + '.' + cur)
            else:
                if isinstance(custom_conf[cur], dict):
                    raise OIJSException(
                        ('FATAL ERROR : configuration {}.{} should be an item. ' + \
                        'A map was found.').format(current_config, cur))

                if isinstance(cur_conf[cur], list):
                    if isinstance(custom_conf[cur], list):
                        cur_conf[cur] = custom_conf[cur]
                    else:
                        cur_conf[cur] = [custom_conf[cur]]
                else:
                    if isinstance(custom_conf[cur], list):
                        if len(custom_conf[cur]) == 1:
                            cur_conf[cur] = custom_conf[cur][0]
                        else:
                            raise OIJSException(
                                ('FATAL ERROR : ' + \
                                'configuration {}.{} should be an item. ' + \
                                'A list was found.').format(current_config, cur)
                            )
                    else:
                        cur_conf[cur] = custom_conf[cur]
        else:
            raise OIJSException(
                'FATAL ERROR : configuration {}.{} does not exist.'.format(
                    current_config, cur))

    return cur_conf


def check_conf_exist():
    """
    check_conf_exist
    """

    if not os.path.exists(os.path.expanduser('~/.oijs')):
        print('Can\'t find config directory. Generating one.')

        os.mkdir(os.path.expanduser('~/.oijs'))

        structure = utils.file_operations.load_dir_structure('oijs.globals.config.dir_structure', 'config_dir.yml')
        utils.file_operations.copy_dir(
            'oijs.misc.oijs_dir',
            os.path.expanduser('~/.oijs'),
            structure['root'],
        )
