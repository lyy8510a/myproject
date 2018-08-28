#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/21 下午2:41.
"""
import os
from flask import Flask
from config.config import config
from backend.urls import register
from backend.models import db  #第二课增加内容
from backend.views import login_manager #第三课增加内容
from flask_login import current_user

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_TEMPLATE_FOLDER = os.path.join(BASE_DIR,'frontend')

def create_app():
    #初始化项目实例
    app = Flask(__name__,template_folder=BASE_TEMPLATE_FOLDER,static_folder=os.path.join(BASE_DIR,'frontend','static'))
    app.secret_key = app.config['SECRET_KEY']

    #导入配置项
    app.config.from_object(config)
    # 注册路由
    register(app)
    # 注册数据库
    db.init_app(app) #第二课增加内容
    #注册登录组件
    login_manager.init_app(app)  #第三课增加内容
    # 将变量注册到jinja全局变量
    app.add_template_global(app.config['PROJECTNAME'], 'PROJECTNAME')
    app.add_template_global(app.config['STATIC_URL'], 'STATIC_URL')


    # 钩子 在请求执行之前
    @app.before_request
    def before_request():
       pass

    return app
