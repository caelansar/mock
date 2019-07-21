# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 上午8:58
# @Author  : Caelansar

from flask import Flask, jsonify, request, abort
from werkzeug.exceptions import HTTPException

from utils import parse_config

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'PUT', 'DELETE', 'POST'])
def dispatch_request(path):
    """
    mock view logic
    :param path: request url for mock server
    :return: response msg that defined in configuration file
    """
    try:
        param = {}
        if request.headers.get('Content-Type') == 'application/json' and request.method in ('POST', 'PUT'):
            param = request.json
        elif request.method == 'GET':
            param = request.args
        else:
            param = request.form
        print(dict(param))
        m = parse_config.filter(url=request.path, method=request.method, param=dict(param))
        return jsonify(m)
    except HTTPException:
        abort(404)

@app.errorhandler(404)
def url_not_found(e):
    return jsonify({
        "code": -1,
        "msg": "the request url not found in mock server"
    })

if __name__ == '__main__':
    app.run()