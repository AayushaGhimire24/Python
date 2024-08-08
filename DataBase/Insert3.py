# to insert
import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('Insert into student(id,name, faculty) values(1, "Ram","BIM"),(2, "Hari","BIM"),(3, "Sita", "BCA")')
conn.commit()
conn.close()