#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# OIJS: cli.cli_complete_helper





import sys
import os
import logging





def getprefix ( available_list, prefix_str ):
	return [ cur_str for cur_str in available_list if cur_str[:len(prefix_str)] == prefix_str ];
