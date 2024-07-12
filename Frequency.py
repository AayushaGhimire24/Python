# WAP to input a character and count it's frequency in a file "abc.txt"
a=input("Enter a character: ")
count=0
f=open("abc.txt","r")
t=f.read()
for x in t:
    if x==a:
        count+=1
print(count)