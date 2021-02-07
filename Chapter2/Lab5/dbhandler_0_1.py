# -*- coding: utf-8 -*-
"""
Lab 5 - dbhandler_0_1.py
Description - ConnectionHandler uses simple sqlite database that contains tables rounds
              containing each rounds to toss dices in a double-or-nothing-game. 
              It plays containing each choices user made (placed bet) and dices output
              when playing a round in the game.
@author - Michalis Iona

"""
import os, argparse
import sqlite3
from sqlite3 import Error

class ConnectionHandler:
    '''simple and naive use of sqlite database'''
    def __init__(self, db):
        self.db = db
        self.connection = None

    def openConnection(self):
        try:        
            self.connection = sqlite3.connect(self.db)#open existing or creates a new
        except Error as error:
            print(error)
            
    def closeConnection(self):
        if self.connection:
            self.connection.close()
            
    def getData(self, query): 
        '''returns a list of tuples'''
        result = [] #fill this in and return it
        cursor = self.connection.cursor() # create cursor
        try:
            cursor.execute(query)
            result = cursor.fetchall()
                
        except Error as error:
            print(error)
        finally:
            cursor.close()      
        return result
       
    def executeScript(self, dicesDB):
        with open("dicesDB.sql", 'r') as sql_file:
            sql_script = sql_file.read()
        self.openConnection()
        try:
            cursor = self.connection.cursor()
            cursor.executescript(sql_script)
            self.connection.commit() #saves the changes
            cursor.close()
        except Error as error:
            self.connection.rollback() #rolls back any changes to the database 
            print(error)
        finally:
            if self.connection:
                self.closeConnection()

def main(path):
    '''funcion to execute the progam, path db name and path to it'''
    c = ConnectionHandler('dicesDB.sqlite')
    c.executeScript('dicesDB.sql')
    c.openConnection()
    
    if c.connection:
        print('connection is open')
        query_1 = 'SELECT * FROM rounds, plays'
        rounds = c.getData(query_1)
        for row in rounds:
            print(row)
        c.closeConnection()

if __name__ == '__main__':
    path = 'dicesDB.sqlite' 
    #if user gives an argument 
    argparser = argparse.ArgumentParser() 
    argparser.add_argument('-i', '--initialize', default=False, required=False)
    args = argparser.parse_args()
    if bool(args.initialize):        
        scriptfile = os.getcwd()+ r'C:\Users\micha\Desktop\OOP\Object_and_Class_Structures\Lab5\dicesDB.sql'
        ConnectionHandler(path).executeScript(scriptfile)
        print(f'database {path} initialized')
    main(path)