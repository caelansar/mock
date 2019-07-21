# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 下午1:57
# @Author  : Caelansar

def validate(req_param, config_param):
    return req_param == config_param


def get_param_form_config(method, api):
    if method == 'POST':
        return api['request'].get('json') or api['request'].get('form')
    else:
        return api['request'].get('param')