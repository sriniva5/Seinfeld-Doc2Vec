# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:38:53 2018

@author: ANANYA_SRINIVASAN
"""

#Flask test
#Trying out the Flask framework to host the search application
#Resource: https://stackoverflow.com/questions/31394998/using-sqlalchemy-to-load-csv-file-into-a-database
#http://www.sqlitetutorial.net/sqlite-import-csv/
#https://github.com/driscollis/flask101/blob/master/Part%20IV%20-%20Adding%2C%20Editing%20and%20Displaying%20Data/models.py

from db_setup import init_db, db_session
from forms import SearchForm
from app import app
from flask import flash, render_template, request, redirect
from models import Data
from tables import Results, Doc2VecResults
from sqlalchemy import or_

import gensim

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    search=SearchForm(request.form) #search form
    if request.method == 'POST':
        return search_results(search)
    
    return render_template('index.html', form=search)
    
@app.route('/results')
def search_results(search):
    results=[]
    search_string=search.data['search']
    
    if search_string:
        if search.data['search']=='':
            query=db_session.query(Data)
            results=query.all()
        else:
            #filter based on user's search (can handle n-grams)
            query=db_session.query(Data).filter(Data.data.contains(search_string))
            results = query.all()
        
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        #display results
        table = Results(results)
        table.border=True
        return render_template('results.html', table=table)
    
@app.route('/item/<int:file>', methods=['GET', 'POST'])
def d2v(file):
    #loading model
    #flash(file) #for testings redirection
    d2v_model = gensim.models.doc2vec.Doc2Vec.load('doc2vec.model')
    inferred_vector=d2v_model.docvecs[int(file)]
    sims=d2v_model.docvecs.most_similar([inferred_vector],topn=len(d2v_model.docvecs))
    
    #split the sims tuples into tags and scores to fetch the corresponding docs
    tags, scores = map(list, zip(*sims))
    tags=list(map(int,tags)) #cast as ints
    
    most_rel=tags[1:11] #getting 10 most related documents
    
    #retrieve the 10 most related documents
    query=db_session.query(Data).filter(or_(Data.file.contains(most_rel[0]), Data.file.contains(most_rel[1]), Data.file.contains(most_rel[2]), 
                                        Data.file.contains(most_rel[3]), Data.file.contains(most_rel[4]), Data.file.contains(most_rel[5]),
                                        Data.file.contains(most_rel[6]), Data.file.contains(most_rel[7]), Data.file.contains(most_rel[8]),
                                        Data.file.contains(most_rel[9])))
    #query=db_session.query(Data).filter(Data.file.contains(m) for m in most_rel)
    
    results=query.all()
    
    if not results:
        #Test to see if the tags were actually generated for the documents
        tags=list(map(str, tags))
        flash(tags[9])
        
        flash('No results found!')
        return redirect('/')
    else:
        table=Doc2VecResults(results)
        table.border=True
        return render_template('doc2vecresults.html', table=table)
    #return redirect('/') #temp solution until we get actual results
    
if __name__ == '__main__':
    app.run()