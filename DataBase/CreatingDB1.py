# Create a database
import sqlite3
conn=sqlite3.connect('test.db')
print('database created')
conn.close()

