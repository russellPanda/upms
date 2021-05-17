#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/17 14:03
# @Author : russell
# @File :  user

import os
import logging
from functools import wraps
from upms.models.permission import User
from upms.models import db
from upms.services.logger import create_logger
from upms.config import basedir

format_str = '%(asctime)s - %(name)s - %(levelname)s --------- %(message)s'
common_logger = create_logger("test", logging.DEBUG, format_str, os.path.join(basedir, 'dev_log.log'))

def is_exist(model):
    """
    :param model: 类型必须得有get_by_name
    :return:
    """
    def decorate(func):

        @wraps
        def wrapper(*args,**kwargs):
            for i in args:
                assert model.get_by_name(i) != None
            return func(*args,**kwargs)
        return wrapper
    return decorate

def is_not_exist(model):
    """
    :param model: 类型必须得有get_by_name
    :return:
    """
    def decorate(func):

        @wraps
        def wrapper(*args,**kwargs):
            for i in args:
                assert model.get_by_name(i) == None
            return func(*args,**kwargs)
        return wrapper
    return decorate



@is_not_exist(User)
def add_user(user_name:str):
    try:
        db.session.add(User(user_name))
        db.session.flush()
    except Exception as e:
        db.session.callback()
        common_logger.error(f'add user error ,{e}',exc_info=True)
    finally:
        db.session.commit()

def delete_user(user_id:str):
    try:
        user=User.get_by_id()
        db.session.delete(user)
        db.session.flush()
    except Exception as e:
        db.session.callback()
        common_logger.error(f'add user error ,{e}',exc_info=True)
    finally:
        db.session.commit()


def update_user(user_name:str):
    pass



