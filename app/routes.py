# -*- coding: utf-8 -*-
__author__ = 'hiepdh2'

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Word"
