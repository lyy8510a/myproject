#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2017/11/8.
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    """Base config class."""
    # 版本
    VERSION = 'beta 0.1'
    # 项目名称
    PROJECTNAME = 'MYPROJECT'
    # 端口
    PORT = 10101

    SECRET_KEY = '1234567890!@#$%^&*()'

class ProdConfig(Config):
    """Production config class."""

    # 是否开启调试
    DEBUG = False
    # 主机ip地址
    HOST = '0.0.0.0'

class SitConfig(Config):
    """Development config class."""
    # Open the DEBUG
    # 是否开启调试
    DEBUG = True
    # 主机ip地址
    HOST = '127.0.0.1'

    # # 数据库配置
    MYSQL_HOST = '127.0.0.1'  #此处修改为您的mysql的主机IP
    MYSQL_PORT = 3306         #此处修改为您的mysql的主机端口
    MYSQL_USER = 'root'       #此处修改为您的mysql的用户名称
    MYSQL_PASS = '123456'     #此处修改为您的mysql的用户密码
    MYSQL_DB = 'myproject'    #此处修改为您的mysql的数据库名称

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(MYSQL_USER, MYSQL_PASS, MYSQL_HOST
                                                                           , MYSQL_PORT, MYSQL_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    pass

# Default using Config settings, you can write if/else for different env
config = SitConfig()