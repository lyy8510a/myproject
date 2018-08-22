#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/22 上午9:40.
"""
from flask import Blueprint,request,render_template,jsonify,flash  #第二课增加内容
from backend.models.UserModel import User
from backend.models import db

#账户的蓝图  访问http://host:port/account 这个链接的子链接，都会跳到这里
account = Blueprint('/account', __name__)  #第二课增加内容

# 访问http://host:port/account/register 这个链接，就会跳到这里
@account.route('/register',methods=(["GET","POST"]))  #第二课增加内容
#上面的链接，绑定的就是这个方法，我们给浏览器或者接口请求 一个json格式的返回
def register():  #第二课增加内容
    if request.method == 'POST':
        form = request.form
        user = User(username=form['username'],email=form['email'],password=form['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify(form)
    return render_template('/account/register.html')