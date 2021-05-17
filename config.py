#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 12:24
# @Author : russell
# @File :  config

import os



basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:  # 基本配置类
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'resources/per.db')
    ITEMS_PER_PAGE = 10
    FLASK_APP = "upms"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'resources/dev.db')
    FLASK_APP = "upms"
    FLASK_ENV='development'


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'resources/test.db')
    WTF_CSRF_ENABLED = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}


