#WAP to input marks in 5 subjects and then calculate total marks,percentage,division and result(pass/fail).
v,w,x,y,z=input("Enter the marks of 5 subjects").split()
a=int (v)
b=int(w)
c=int(x)
d=int(y)
e=int(z)
sum=a+b+c+d+e
print("Total marks is: ",sum)
per=(sum//5)
print("Percentage is: ",per)

if a>=50 and b>=50 and c>=50 and d>=50 and e>=50:
    print ("Pass")
    if per>=80:
        print("Distinction")
    elif per>=70:
        print("First Division")
    else: 
        print("Second division")
else:
    print("Fail")




