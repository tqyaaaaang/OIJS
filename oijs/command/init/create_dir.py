#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.init.create_dir


"""
module oijs.command.init.create_dir
"""


import logging
import os
import sys
import shutil
import yaml

from oijs.globals.log import log_decorator
from oijs import utils
from oijs.globals import exceptions

gl = logging.getLogger('global')   # pylint: disable=C0103


class file_exist_exception(exceptions.OIJSException):   # pylint: disable=C0103
    """
    class file_exist_exception
    """

    def error_msg(self):
        """
        error_msg
        """

        return ('ERROR : File \'{}\' exists. Init failed. ' + \
                'If you still want to init, use --force option').format(
                    self.args[0])


@log_decorator.log_func
def create_dir(src, dst, config_module, config_filename, force=False):
    """
    create_dir

    Arguments:
    - src: source directory
    - dst: destination directory
    - config_module: module containing the config file
        e.g. oijs.command.init.dir_structure
    - config_filename: config filename
        e.g. problem_dir.yml
    """

    gl.debug('creating directory, source = \'%s\', ' + \
             'destination = \'%s\', force = \'%s\'',
             src, dst, force)

    structure = utils.file_operations.load_dir_structure(config_module, config_filename)

    gl.debug('load directory structure succeeded')

    try:
        utils.file_operations.copy_dir(src, dst, structure['root'], force, file_exist_exception)
    except file_exist_exception as err:
        gl.error(err.error_msg())
        print(err.error_msg(), file=sys.stderr)
