# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:50:08 2018

@author: ANANYA_SRINIVASAN
"""

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///myseinfeld.db', echo=True)
Base = declarative_base()

class Quotes(Base):
    __tablename__="quotes"
    file=Column(Integer, primary_key=True)
    data=Column(String)
    
Base.metadata.create_all(engine)