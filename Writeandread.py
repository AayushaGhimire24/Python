# WAP to input a line of text, store it in a file and then read from the file to display it's content
f=open("question.txt","w")
t=input("Enter a sentence")
f.write(t)
f.close()

f=open("question.txt","r")
print(f.read())
f.close()