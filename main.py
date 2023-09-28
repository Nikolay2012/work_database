#import library for work with data base
import sqlite3
import os
import modules.create_column as m_function
import modules.create_table as m_table
import modules.create_column as m_column
import modules.delete_table as m_delete
import modules.change_table_column as m_change
import modules.gets_the_entry as m_gets
# Search path to folder database
path = os.path.abspath(__file__ + '/../database')
# Sets direction to keep files in database
os.chdir(path)
# Create connection to data base
connection = sqlite3.connect('data_base.db')
# Creating the object to save data in database
cursor = connection.cursor()
# Set command for variable which creates the table
# new_table = 'CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY)'
# Execute command that creates table  
cursor.execute(m_table.create_table(name_table= "Trees"))
# Set command for variable where we add the column  
# cursor.execute(m_column.create_column(column_name= "name", column_type= "TEXT", name_table= "Trees"))

# cursor.execute(m_delete.delete_table(name_table= "Users"))

# cursor.execute(m_change.change_table(table_name= "Trees", column_name= "name"), ("Mykola", "Mykola"))
a = cursor.execute(m_gets.retrieves_the_entry(new_column= "name", new_table= "Trees")).fetchall()
print(a)

# save changes
connection.commit()
# close our connection to data base
connection.close()