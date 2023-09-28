import sqlite3
#  створює функції в окремому модулі що отримує запис з конкретної таблиці та конкретного стовбчика та записує до змінної 


def retrieves_the_entry(new_table, new_column):
  query = f"SELECT {new_column} FROM {new_table}"
  return query
