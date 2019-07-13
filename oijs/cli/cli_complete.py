#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_complete


"""
module oijs.cli.cli_complete
"""


from oijs.cli import cli_complete_helper


def complete(text, line, begidx, endidx):   # pylint: disable=W0613
    """
    complete
    """

    return []


def complete_names(text, line, begidx, endidx):   # pylint: disable=W0613
    """
    complete_names
    """

    available_list = [
        'help',
        'exit',
        'init',
        'judge'
    ]

    return cli_complete_helper.getprefix(available_list, text)
