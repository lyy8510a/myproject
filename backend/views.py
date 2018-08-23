#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/21 下午3:51.
"""
from flask_login import LoginManager  #第三课新增



# Set up Flask-Login
login_manager = LoginManager()  #第三课新增
login_manager.session_protection = 'strong'  #第三课新增
login_manager.login_view = 'account.login'  #第三课新增

