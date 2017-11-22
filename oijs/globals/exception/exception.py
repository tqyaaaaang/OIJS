#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.exception.exception


"""
module oijs.globals.exception.exception
"""


class oijs_exception(Exception):   # pylint: disable=C0103
    """
    class oijs_exception
    """

    def error(self):
        """
        error
        """

        return self.args[0]


class RET_FATAL_exception(Exception):   # pylint: disable=C0103
    """
    class RET_FATAL_exception
    """

    pass
