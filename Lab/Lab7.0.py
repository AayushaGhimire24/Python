# Write a program to insert any 5 records (id, name, address, faculty) to a table 'student'.
# Create a database
import sqlite3
conn=sqlite3.connect('Lab7.db')
print('database created')

conn.execute('create table student(id int primary key not null, name varchar(20) not null,address varchar(50) not null, faculty varchar(20) not null)')
print('table creation successful')

conn.execute('Insert into student(id,name,address,faculty) values(1, "Ram","Kathmandu","BIM"),(2, "Hari","Bhaktapur","BIM"),(3, "Sita","Janakpur","BCA"),(4, "Sanskriti","US","BIT"),(5,"Tina","Mumbai","BCA")')
conn.commit()
conn.close()
print("record inserted successfully")