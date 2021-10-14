# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:04:33 2021

@author: 1
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')