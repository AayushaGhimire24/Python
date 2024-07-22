# WAP to print all files inside a directory that have a ".txt" extension
import os
files=os.listdir("./")
for file in files:
    if file.lower().endswith(".txt"):
        print(file)