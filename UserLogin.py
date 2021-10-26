# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:52:36 2021

@author: Alina Shcherbinina
"""

from flask_login import UserMixin

class UserLogin(UserMixin):
    
    def fromDB(self, user_id, db):
        self.__user = db.getUser(user_id)
        return self 
    
    def create(self, user):
        self.__user = user
        return self 
    
    def get_id(self):
        return str(self.__user['id'])

