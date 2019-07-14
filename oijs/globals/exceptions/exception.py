#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: globals.exceptions.exception


"""
module oijs.globals.exceptionss.exception
"""


class OIJSException(Exception):   # pylint: disable=C0103
    """
    class OIJSException
    """

    def error_msg(self):
        """
        error_msg
        """

        return self.args[0]


class RET_FATAL_exception(OIJSException):   # pylint: disable=C0103
    """
    class RET_FATAL_exception
    """

    pass
