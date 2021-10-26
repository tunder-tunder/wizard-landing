# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:04:33 2021

@author: Alina Shcherbinina 
"""
import sqlite3
import os
from flask import Flask
from flask import render_template, request, flash, g, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user
from flask_login import logout_user
from FDataBase import FDataBase
from UserLogin import UserLogin


DATABASE = '/tmp/wizsite.db'
DEBUG = True

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdkpwoekf0293rjkd&WE'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(__name__) 

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'wizsite.db')))

login_manager = LoginManager(app)
login_manager.login_view = 'AdminLogin'
login_manager.login_message_category = 'error'

@login_manager.user_loader
def load_user(user_id):
    print("load_user")
    return UserLogin().fromDB(user_id, dbase)



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
        
dbase = None 
@app.before_request
def before_request_func():
    global dbase 
    db= get_db()
    dbase = FDataBase(db)


@app.route('/#form', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
        
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


@app.route("/admin", methods=["POST", "GET"])
def AdminLogin():
    if current_user.is_authenticated:
        return redirect(url_for('showTable'))
    
    if request.method == "POST":
        user = dbase.getUserName(request.form['name'])
        if user and check_password_hash(user['pasw'], request.form['passw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('showTable'))
        
        flash("wrong password or username", "error")
        
    return render_template("login.html")


@app.route("/admin/views")
@login_required
def showTable():
    return render_template('admin.html', posts = dbase.getPosts())
   
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out! (* ^ ω ^)", "success")
    return redirect(url_for('AdminLogin'))

if __name__ == "__main__":
    print(generate_password_hash("jemmathebestdog1"))
    app.run(debug=True)
    
 