# -*- coding: utf-8 -*-
__author__ = 'hiepdh2'
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = dict(username='Mr Hiep')
    posts = [dict(author=dict(username='Mr Hiep'), body='Beautiful day'),
             dict(author=dict(username='Mr Nam'), body='Bad day')]
    return render_template('index.html', title='Home page', user=user, posts=posts)
