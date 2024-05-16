#WAP to input marks in 3 subjects and calculate total marks,percentage,result(pass/fail) and division
a=int(input("Enter marks of 1st Subject"))
b=int(input("Enter marks of 2nd Subject"))
c=int(input("Enter marks of 3rd Subject"))
t=a+b+c
p=t/3
print("total Marks=",t)
# print("Percntage=",round(p))
print("Percntage=",round(p,2))
if a>=50 and b>=50 and c>=50:
    print('pass')
    if p>=80 :
       print('distinction')
    elif p>=60:
        print('first division')
    else :
        print("Second Division")
else :
    print('fail')





