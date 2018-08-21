#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/21 下午3:51.
"""
from flask import Blueprint,jsonify

#账户的蓝图  访问http://host:port/account 这个链接的子链接，都会跳到这里
account = Blueprint('/account', __name__)

# 访问http://host:port/account/test 这个链接，就会跳到这里
@account.route('/test')
#上面的链接，绑定的就是这个方法，我们给浏览器或者接口请求 一个json格式的返回
def test():
    return jsonify({'code':0,'content':'hi flask'})