# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:07:15 2018

@author: ANANYA_SRINIVASAN
"""

#db_setup.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#import pandas as pd

engine = create_engine('sqlite:///myseinfeld.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base=declarative_base()
Base.query=db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
    
    #file_name = 'test.csv'
    #df = pd.read_csv(file_name)
    #df.to_sql(con=engine, index_label='File', name=myseinfeld.__tablename__, if_exists='replace')
