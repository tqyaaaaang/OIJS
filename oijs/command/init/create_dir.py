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

gl = logging.getLogger('global')   # pylint: disable=C0103


class file_exist_exception(Exception):   # pylint: disable=C0103
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
def create_dir(src, dst, config_filename, force=False):
    """
    create_dir
    """

    gl.debug('creating directory, source = \'%s\', ' + \
             'destination = \'%s\', force = \'%s\'',
             src, dst, force)

    structure = {}
    with open(config_filename) as config_file:
        structure = yaml.load(config_file, Loader=yaml.FullLoader)

    gl.debug('load directory structure succeeded')

    try:
        _create_dir_recursive(src, dst, structure['root'], force)
    except file_exist_exception as err:
        gl.error(err.error_msg())
        print(err.error_msg(), file=sys.stderr)


@log_decorator.log_func
def _create_dir_recursive(src, dst, structure, force=False, cur_dir=''):   # pylint: disable=R0912
    """
    _create_dir_recursive
    """

    if structure == 'EMPTY_DIR':
        return

    gl.debug('creating directory in \'%s\'', cur_dir)
    for iterator in structure:
        if isinstance(iterator, (list, tuple, dict)):
            for val in iterator:
                cur_key = val
            element = cur_key
            target = os.path.join(dst, element)
            if os.path.exists(target):
                if os.path.isfile(target):
                    gl.debug('\'%s\' is an existing file',
                             os.path.join(cur_dir, element))
                    if not force:
                        raise file_exist_exception(
                            os.path.join(cur_dir, element))
                    else:
                        gl.debug('Detected option force, remove the file')
                        os.remove(target)
            if not os.path.exists(target):
                gl.debug('Creating directory \'%s\'',
                         os.path.join(cur_dir, element))
                os.mkdir(target)
            _create_dir_recursive(
                os.path.join(src, element),
                os.path.join(dst, element),
                iterator[element],
                force,
                os.path.join(cur_dir, element)
            )
        else:
            element = iterator
            target = os.path.join(dst, element)
            if os.path.exists(target):
                gl.debug('\'%s\' exists',
                         os.path.join(cur_dir, element))
                if not force:
                    raise file_exist_exception(os.path.join(cur_dir, element))
                else:
                    gl.debug('Detected option force, remove it')
                    if os.path.isfile(target):
                        os.remove(target)
                    else:
                        shutil.rmtree(target)
            shutil.copy(os.path.join(src, element), target)
