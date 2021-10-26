# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:09:15 2021

@author: Alina Shcherbinina
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField, TelField

class InfoForm(FlaskForm):
    name = StringField("name: ", validators=[DataRequired(), Length(min=1, max=100)])  
    telephone = TelField("tele:", validators=[DataRequired(), Length(min=11, max=11)])
    email = EmailField("Email: ", validators=[Email(), DataRequired()])     
    company = StringField("company: ", validators=[Length(min=3, max=100)])  
    address = StringField("address: ", validators=[Length(min=3, max=100)])  
    comment = TextAreaField("comment: ")
    submit = SubmitField("Сделать заказ")