x,y,z=input('enter the numbers').split()
a=int(x)
b=int(y)
c=int(z)
if a>b and a<c:
    print("middle number=",a)
elif b>a and b<c:
    print ("middle numbner=",b)
else:
        print ("middle number:",c)
