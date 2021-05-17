#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 18:34
# @Author : russell
# @File :  utils

import json



def dict_2json(d:dict):
    return json.dumps(d,ensure_ascii=False)


def list_2json(l:list):
    return json.dumps(l)

def page_index(page:int,size:int):
    """
    1 10 0-9
    2 2  2-3
    :param page:
    :param size:
    :return:
    """

    return slice((page-1)*size,page*size,1)