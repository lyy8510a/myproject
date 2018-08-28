#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/23 上午11:09.
"""
from flask import Blueprint,render_template
from backend.account.views import login_required
from utils.layout import layout
admin = Blueprint('admin', __name__)



@admin.route('/')
def index():
    return layout('/base/index.html')