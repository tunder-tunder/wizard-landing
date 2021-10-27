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
    name = StringField("Ваше имя: ", validators=[DataRequired("Пожалуйста, заполните это поле"), Length(min=2, max=100, message=("Имя должно быть больше двух символов"))])  
    telephone = TelField("Телефон:", validators=[DataRequired("Пожалуйста, заполните это поле"), Length(min=11, max=11,  message=("Неверный номер телефона"))])
    email = EmailField("Email: ", validators=[Email("Пожалуйста, проверьте правильность написания электронной почты"), DataRequired("Пожалуйста, заполните это поле")])     
    company = StringField("Компания: ", validators=[])  
    address = StringField("Адреc: ", validators=[Length(min=5, max=100,  message=("Адрес должен быть больше пяти символов"))])  
    comment = TextAreaField("Комментарий: ")
    submit = SubmitField("Сделать заказ")