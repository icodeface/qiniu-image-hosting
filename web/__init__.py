# -*- coding: utf-8 -*-
"""
__author__ = 'CodeFace'
"""
from flask import Flask
import logging

app = Flask(__name__)
app.config.from_object('config')

file_handle = logging.FileHandler(app.config['LOG_FILE'])
file_handle.setLevel(logging.WARNING)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
file_handle.setFormatter(logging_format)
app.logger.addHandler(file_handle)

# 如果设为True，/path 和 /path/ 会被认为是两个不同的地址
app.url_map.strict_slashes = False

import web.views

