#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.commands.judge


"""
module oijs.cli.commands.judge
"""


import os

from ...command.judge import judge as real_judge
from ...globals.log import log_decorator
from ...globals.data import global_arguments


@log_decorator.log_func
def judge():
    """
    judge
    """

    real_judge.judge(
        problem_dir=os.path.abspath(global_arguments.global_arg.directory),
        submission_dir=os.path.abspath(
            os.path.join(
                global_arguments.global_arg.directory,
                'submission',
                str(global_arguments.current_arg.submission_id)
            )
        )
    )
