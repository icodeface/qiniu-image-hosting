# -*- coding: utf-8 -*-
"""
__author__ = 'CodeFace'
"""
from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
from web import app
from web.utils import push, allowed_file
from urllib.parse import urljoin
from config import DOMAIN


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        file_name = secure_filename(file.filename)
        ret, info = push(file, file_name)
        return jsonify({
            'code': 0,
            'url': urljoin(DOMAIN, ret.get('key'))
        })
    return jsonify({
        'code': 1
    })
