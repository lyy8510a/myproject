#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/21 下午3:50.
"""
from backend.account.views import account
from backend.admin.views import admin

# 蓝图注册
def register(app):
    app.register_blueprint(account, url_prefix='/account', strict_slashes=False)
    app.register_blueprint(admin, url_prefix='/admin', strict_slashes=False)