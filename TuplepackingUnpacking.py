fruits=('Apple','Orange','Mango')#Packing
a,b,c=fruits#Unpacking
print(a)
print(b)
print(c)

#We can use '*' symbol with variable name to get the remaining data items
fruits=('Apple','Orange','Mango')
a,*b=fruits#Unpacking
print(a)
print(b)

fruits=('Apple','Mango','Grapes','Cherry','Orange')
a,*b,c=fruits
print(a)
print(b)
print(c)