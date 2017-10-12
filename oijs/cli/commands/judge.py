#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.judge





import logging

from ...command.judge import judge as real_judge
from ...globals.log import log_decorator





@log_decorator.log_func
def judge ():
	real_judge.judge ()
