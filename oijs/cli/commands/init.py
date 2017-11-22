#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.init


"""
module oijs.cli.commands.init
"""


from ...command.init import init as real_init
from ...globals.log import log_decorator


@log_decorator.log_func
def init():
    """
    init
    """

    real_init.init()
