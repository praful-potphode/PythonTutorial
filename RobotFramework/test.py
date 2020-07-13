import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=test_database.accdb;')
cursor = conn.cursor()
cursor.execute('select * from names_table')

for row in cursor.fetchall():
    print(row)
