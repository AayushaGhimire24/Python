# WAP to input a line of text, store in a file and then read from the file to display its content.
f=open("Lab.txt","w")
t=input("Enter a sentence: ")
f.write(t)
f.close()

f=open("Lab.txt","r")
print(f.read())
f.close()