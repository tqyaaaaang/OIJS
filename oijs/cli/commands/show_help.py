#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.show_help





import logging

from ...command.help import show_help as real_show_help





def show_help ():
	real_show_help.show_help ()
