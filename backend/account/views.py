#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/22 上午9:40.
"""
from flask import Blueprint,request,render_template,jsonify,flash  #第二课增加内容
from flask import redirect,url_for,current_app
from backend.models.UserModel import User
from backend.models import db
from flask_login import login_user,login_required,logout_user #第三课增加内容


#账户的蓝图  访问http://host:port/account 这个链接的子链接，都会跳到这里
account = Blueprint('account', __name__)  #第二课增加内容

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

@account.route('/login',methods=(["GET","POST"]))
def login(): #第三课内容
    if request.method == "POST":
        form = request.form #获取登录表单
        user = User.query.filter_by(username=form['username']).first()  #查出用户信息
        if user is not None and user.password_hash is not None and user.verify_password(form['password']):  #检查密码是否正确
            login_user(user,True)  #登录操作
            flash('You are now logged in. Welcome back!', 'success')
            return redirect( url_for(request.args.get('next') or 'admin.index'))
        else:
            flash('Invalid email or password.', 'error')
    return render_template('/account/login.html')

@account.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('admin.index'))

