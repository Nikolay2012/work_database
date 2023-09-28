def change_table(table_name: str, column_name: str):
    a = f"INSERT INTO {table_name} ({column_name}, {column_name}) VALUES (?, ?)"
    # "INSERT INTO Trees (name, surname) VALUES (?, ?)", ("Mykola", "Mykola")
    return a