#wap to check armstrong or not
n=int(input("Enter a number"))
sum=0
org=n
while n>0:
     r=n%10
     sum=sum+r**3
     n=n//10
if sum==org:
     print('it is Armstrong')
else:
     print('It is not Armstrong')