#WAP to input 2 numbers and print the smaller one
x,y=input('enter the numbers').split()
a=int(x)
b=int(y)
if a<b:
    print('smaller:',a)
else:
    print('smaller:',b)
