#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/23 上午11:09.
"""
from flask import Blueprint,render_template
from backend.account.views import login_required

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    return render_template('/base/index.html')