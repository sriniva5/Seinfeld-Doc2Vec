# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:25:55 2018

@author: ANANYA_SRINIVASAN
"""

#tables.py

from flask_table import Table, Col, LinkCol

class Results(Table):
    dir=LinkCol('Doc2Vec', 'd2v', url_kwargs=dict(file='file')) #link to the doc2vec results; corresponding column, function, and url
    file=Col('File')
    data=Col('Data')
    
class Doc2VecResults(Table):
    file=Col('File')
    data=Col('Data')