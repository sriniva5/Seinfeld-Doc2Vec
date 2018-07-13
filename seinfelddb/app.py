# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:00:48 2018

@author: ANANYA_SRINIVASAN
"""

#App.py testing the database

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myseinfeld.db'
app.secret_key="WHY"

db=SQLAlchemy(app)