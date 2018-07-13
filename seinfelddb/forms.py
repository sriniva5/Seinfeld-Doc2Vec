# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:36:32 2018

@author: ANANYA_SRINIVASAN
"""

#forms.py

from wtforms import Form, StringField, SelectField

class SearchForm(Form):
    choices=[('Quotes', 'Quotes')]
    select=SelectField('Search for Seinfeld quotes:', choices=choices)
    search=StringField('')
    