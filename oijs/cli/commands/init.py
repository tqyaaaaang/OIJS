#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.init





import logging

from ...command.init import init as real_init
from ...globals.log import log_decorator





@log_decorator.log_func
def init ():
	real_init.init ()
