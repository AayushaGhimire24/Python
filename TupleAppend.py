#Adding&modifying item to a tuple
a=("Apple","Orange")
b=list(a)
#b[0]='cherry'#to edit the name
b.append("Mango")    
a=tuple(b)
print(a)

