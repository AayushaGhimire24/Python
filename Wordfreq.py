# WAP to input a word  and count its frequency in a file "abc.txt"
a=input("Enter a word")

f=open("abc.txt","r")
t=f.read().split()
print(t.count(a))
f.close()

