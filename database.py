#import library for work with data base
import sqlite3
import os
# Search path to folder database
path = os.path.abspath(__file__ + '/../database')
# Sets direction to keep files in database
os.chdir(path)
# create connection to data base
connection = sqlite3.connect('data_base.db')
# creating the object to save data in database
cursor = connection.cursor()
# set command for variable which creates the table
new_table = 'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY)'
# execute command that creates table  
cursor.execute(new_table)
# set command for variable where we add the column  
create_name = 'ALTER TABLE Users ADD COLUMN name TEXT'
# execute command that create name
cursor.execute(create_name)
# save changes
connection.commit()
# close our connection to data base
connection.close()