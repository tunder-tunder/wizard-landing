# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:04:33 2021

@author: Alina Shcherbinina 
"""
import sqlite3
import os
from flask import Flask
from flask import render_template, request, flash, g
from FDataBase import FDataBase


DATABASE = '/tmp/wizsite.db'
DEBUG = True

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdkpwoekf0293rjkd&WE'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(__name__) 

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'wizsite.db')))

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn 
   
    
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()
    

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db 

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/#form', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    db= get_db()
    dbase = FDataBase(db)
        
    if request.method == 'POST':
        
        if len(request.form['name']) > 2:
            res = dbase.addPost(request.form['name'], 
                              request.form['tele'], 
                              request.form['email'],
                              request.form['company'],
                              request.form['address'],
                              request.form['comment'])
            if not res:
                flash('Ошибка отправки', category='error')
            else:
                flash('Сообщение отправлено', category='success')
        else: 
            flash('Ошибка отправки', category='error')
        
    
    return render_template('index.html');

@app.route("/admin")
def showTable():
    
    db= get_db()
    dbase = FDataBase(db)
    
    return render_template('admin.html', posts = dbase.getPosts())
   


if __name__ == "__main__":
    app.run(debug=True)
    
 