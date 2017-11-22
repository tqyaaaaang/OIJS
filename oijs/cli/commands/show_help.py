#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.show_help


"""
module oijs.cli.commands.show_help
"""


from ...command.help import show_help as real_show_help
from ...globals.log import log_decorator


@log_decorator.log_func
def show_help():
    """
    show_help
    """

    real_show_help.show_help()
