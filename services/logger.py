#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 14:34
# @Author : russell
# @File :  logger

import os
import logging
from upms.config import basedir

def create_logger(name: str, level_int: int, formatter_str: str, log_path:str , stream=True):
    logger = logging.getLogger(name)
    # level
    logger.setLevel(level=level_int)
    # Formatter
    formatter = logging.Formatter(formatter_str)
    # FileHandler
    if log_path:
        fh = logging.FileHandler(log_path)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    # StreamHandler
    if stream:
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)
    return logger


# format_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# common_logger = get_logger("test", logging.DEBUG, format_str,  os.path.join(basedir,'dev_log.log'))