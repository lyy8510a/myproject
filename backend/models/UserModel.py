#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/22 下午1:50.
"""
from flask_login import UserMixin,AnonymousUserMixin  #第二课增加内容
from werkzeug.security import check_password_hash, generate_password_hash  #第二课增加内容
from backend.models import db  #第二课增加内容
from backend.views import login_manager #第三课新增
from flask import current_app #第五课内容


class Permission: #第五课内容
    GENERAL = 0x01
    ADMINISTER = 0xff

class Role(db.Model): #第五课内容
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    index = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.GENERAL, 'main', True),
            'Administrator': (
                Permission.ADMINISTER,
                'admin',
                False  # grants all permissions
            )
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.index = roles[r][1]
            role.default = roles[r][2]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role \'%s\'>' % self.name



class User(UserMixin, db.Model):  #第二课增加内容
    __tablename__ = 'users'  #这是我们将来建出来的表的表名，在这里定义，下面的都是字段名和字段类型长度这些
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  #第五课内容

    def __init__(self, **kwargs): #第五课内容
        super(User, self).__init__(**kwargs)
        print(self)
        if self.role is None:
            if self.username == current_app.config['ADMIN_USER'] or self.email == current_app.config['ADMIN_EMAIL']:
                self.role = Role.query.filter_by(
                    permissions=Permission.ADMINISTER).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def can(self, permissions): #第五课内容
        return self.role is not None and \
            (self.role.permissions & permissions) == permissions

    def is_admin(self): #第五课内容
        return self.can(Permission.ADMINISTER)


    #脱敏
    @property
    def password(self):  #第二课增加内容
        raise AttributeError('`password` is not a readable attribute')
    #加密
    @password.setter
    def password(self, password):  #第二课增加内容
        self.password_hash = generate_password_hash(password)
    #校验密码
    def verify_password(self, password):  #第二课增加内容
        return check_password_hash(self.password_hash, password)
    #查询返回的格式
    def __repr__(self):  #第二课增加内容
        return '<User \'%s\'>' % self.username

class AnonymousUser(AnonymousUserMixin): #第三课新增
    def can(self, _):
        return False

    def is_admin(self):
        return False


login_manager.anonymous_user = AnonymousUser   #第三课新增


@login_manager.user_loader
def load_user(user_id): #第三课新增
    return User.query.get(int(user_id))