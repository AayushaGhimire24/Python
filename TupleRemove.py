#Removing item from a tuple
a=("Apple","Orange","Cherry")
b=list(a)
b.remove("Apple")    
a=tuple(b)
print(a)
