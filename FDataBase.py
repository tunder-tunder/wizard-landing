# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:11:17 2021

@author: Alina Shcherbinina
"""
import shortuuid
import sqlite3
import string
import random


alphabet = string.ascii_lowercase + string.digits
su = shortuuid.ShortUUID(alphabet=alphabet)

class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()
        
    def getForm(self):
        sql = ''' SELECT * FROM mainmenu '''
        try: 
            self.__cur.execute(sql)
            res = self.__cur.fetchcall()
            if res: return res
        except:
            print("Error reading data base")
        return [] 
    
    def addPost(self, name, tele, email, company, address, comment):
        try: 
            uid = su.random(length=8)
            self.__cur.execute("INSERT INTO mainmenu VALUES(NULL, ?, ?,?,?,?,?,?)", (uid, name, tele, email, company, address, comment))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error adding an entry" + str(e))
            return False
        
        return True
        