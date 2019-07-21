# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 上午9:31
# @Author  : Caelansar

import json

from werkzeug.exceptions import HTTPException

from utils.params import validate, get_param_form_config


def parse():
    with open('api.json') as f:
        d = json.load(f)
        return d


def filter(url, method, param):
    print(url, method)
    api_configs = parse()
    for api in api_configs:
        if api['request']['url'] == url and api['request']['method'] == method \
                and validate(param, get_param_form_config(method, api)):
            return api['response']['json']
    raise HTTPException(response=404)

if __name__ == '__main__':
    parse()