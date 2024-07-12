# WAP to copy content of "abc.txt" into "xyz.txt".
f=open("abc.txt","r")
a=f.read()
f.close()
f=open("xyz.txt","w")
f.write(a)
f.close()