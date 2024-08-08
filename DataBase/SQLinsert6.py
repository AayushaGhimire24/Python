# python script to insert record
import mysql.connector
conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="pythondb"
)
mycursor=conn.cursor()
mycursor.execute('Insert into student(id,name, faculty) values(1, "Geeta","BIM"),(2, "Shyam","BBS"),(3, "Aayu", "BBA")')
conn.commit()
conn.close()