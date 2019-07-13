#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: main


"""
module oijs.main
"""


from oijs.cli import cli_main
from oijs.globals.data import data
from oijs.globals.config import config
from oijs.cli.arguments import get_arguments


def main():
    """
    main
    """

    data.load_data()
    config.load_conf()
    get_arguments.init_parsers()

    cli_main.cli_run()


if __name__ == '__main__':
    main()
