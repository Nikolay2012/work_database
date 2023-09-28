def create_column(column_name: str, column_type: str, name_table: str):
    return (f"ALTER TABLE {name_table} ADD COLUMN {column_name} {column_type}")
    
