#!/usr/bin/env python3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: utils.file_operations


"""
module oijs.utils.file_operations
"""


import os
import yaml
import shutil
import logging

try:
    import importlib.resources as pkg_resources
except ImportError:
    import importlib_resources as pkg_resources

from oijs.globals.log import log_decorator

gl = logging.getLogger('global')   # pylint: disable=C0103


@log_decorator.log_func(logger_may_not_exist=True)
def load_dir_structure(desc_module_name, desc_file_name):
    """
    load_dir_structure
    """
    structure = {}
    with pkg_resources.open_text(desc_module_name, desc_file_name) as config_file:
        structure = yaml.load(config_file, Loader=yaml.FullLoader)
    return structure


@log_decorator.log_func(logger_may_not_exist=True)
def copy_dir(src, dst, structure, force=False, exception=Exception):
    """
    copy_dir
    """
    _copy_dir_recursive(src, dst, structure, force, '', exception)


@log_decorator.log_func(logger_may_not_exist=True)
def _copy_dir_recursive(src, dst, structure, force=False, cur_dir='', exception=Exception):   # pylint: disable=R0912
    """
    _copy_dir_recursive
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
                        raise exception(
                            os.path.join(cur_dir, element))
                    else:
                        gl.debug('Detected option force, remove the file')
                        os.remove(target)
            if not os.path.exists(target):
                gl.debug('Creating directory \'%s\'',
                         os.path.join(cur_dir, element))
                os.mkdir(target)
            _copy_dir_recursive(
                src + '.' + element,
                os.path.join(dst, element),
                iterator[element],
                force,
                os.path.join(cur_dir, element),
				exception
            )
        else:
            element = iterator
            target = os.path.join(dst, element)
            if os.path.exists(target):
                gl.debug('\'%s\' exists',
                         os.path.join(cur_dir, element))
                if not force:
                    raise exception(os.path.join(cur_dir, element))
                else:
                    gl.debug('Detected option force, remove it')
                    if os.path.isfile(target):
                        os.remove(target)
                    else:
                        shutil.rmtree(target)
            with pkg_resources.open_text(src, element) as SRC:
                with open(target, 'w') as DST:
                    shutil.copyfileobj(SRC, DST)
