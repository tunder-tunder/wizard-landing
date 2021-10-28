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
        
    def getPosts(self):
        try: 
            self.__cur.execute("SELECT * FROM mainmenu")
            res = self.__cur.fetchall()
            if res: return res
        except sqlite3.Error as e:
            print("Error reading data base" + str(e))
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
    
    def getUser(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False 
            
            return res
        except sqlite3.Error as e:
            print("Error of getting data from DB" + str(e))
            
        return False
    
    def getUserName(self, name):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE login = '{name}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False 
            
            return res
        except sqlite3.Error as e:
            print("Error of getting data from DB" + str(e))
            
        return False
    
    def getUserUid(self, name):
        try:
            self.__cur.execute(f"SELECT uid FROM users WHERE login = '{name}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("User not found")
                return False 
            
            return res
        except sqlite3.Error as e:
            print("Error of getting data from DB" + str(e))
            
        return False
        