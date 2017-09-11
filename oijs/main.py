#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: main





from .cli import cli_main
from .globals.data import data
from .globals.config import config





def main ():
	data.load_data ()
	config.load_conf ()
	cli_main.cli_run ()





if __name__ == '__main__':
	main ()
