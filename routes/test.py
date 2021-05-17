#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# @Time : 2021/5/13 17:17
# @Author : russell
# @File :  test

import os

import json
import logging
from flask import Blueprint, request, jsonify, make_response, abort,current_app,render_template
from jinja2 import TemplateNotFound

index_bp = Blueprint('index', __name__)

@index_bp.route('/u')
def show():
    return """<html>
    <head>
        <title>Index</title>
    </head>
    <body>
        <h1>调试页 面</h1>
    </body>
</html>"""
