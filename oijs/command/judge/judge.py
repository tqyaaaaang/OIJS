#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: command.judge.judge





import sys
import os
import logging

from ...globals.data import global_arguments
from ...globals.log import log_decorator

gl = logging.getLogger ( 'global' )





@log_decorator.log_func
def judge ():
	print ( 'judge' )
