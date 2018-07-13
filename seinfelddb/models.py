# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:03:18 2018

@author: ANANYA_SRINIVASAN
"""

#models.py

from app import db

class Data(db.Model):
    __tablename__="test"
    
    file=db.Column(db.Integer, primary_key=True)
    data=db.Column(db.String)
    
    def __repr__(self):
        return "{}".format(self.name)