# WAP to print all files inside a directory that begin with 'A' or 'a'
import os
files=os.listdir("./")
for file in files:
 if file.lower().startswith('a'):
   print(file)