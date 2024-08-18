#WAP a program to input a number,find it's reverse and then check whether it is palindrome or not
n=int(input("Enter a number: "))
sum=0
org=n
while n>0:
     r=n%10
     sum=sum*10+r
     n=n//10
if sum==org:
     print('It is palindrome')
else:
     print('It is not palindrome')