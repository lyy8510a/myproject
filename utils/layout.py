#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
Created by liaoyangyang1 on 2018/8/24 下午5:10.
"""


from flask import render_template,request,jsonify #第五课增加内容


def layout(template_name_or_list,**context): #第五课增加内容
    return render_template(template_name_or_list,
                           tag = request.url.split('/')[-2],
                           **context)


def outputnJsoByMessage(isSuccess,message): #第五课增加内容
    dict = {}
    dict['isSuccess'] = isSuccess if isSuccess else 0
    dict['message'] = isSuccess if isSuccess else ' '
    return jsonify(dict)

