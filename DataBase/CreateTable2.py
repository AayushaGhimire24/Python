# create a table in above db
import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('create table student(id int primary key not null, name varchar(20) not null,faculty varchar(20) not null)')
print('table creation successful')
conn.close()

