#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 14:55
# @Author : russell
# @File :  user

import os

import json
import logging
from flask import Blueprint, request, jsonify, make_response, render_template
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from upms.models.permission import User, Ability, Role
from upms.models import db
from upms.config import basedir
from upms.services.logger import create_logger
from upms.services.utils import dict_2json, list_2json, page_index

format_str = '%(asctime)s - %(name)s - %(levelname)s --------- %(message)s'
common_logger = create_logger("test", logging.DEBUG, format_str, os.path.join(basedir, 'dev_log.log'))

user_bp = Blueprint('user', __name__)

user_api = Api(user_bp)

class UserProfileResource(Resource):
    def get(self,id):
        pass


    def put(self,id):
        pass

    def delete(self,id):
        pass

    def post(self):
        pass


user_api.add_resource(UserProfileResource, '/upms/api/v1.0/user/<init:id>', endpoint='user')



