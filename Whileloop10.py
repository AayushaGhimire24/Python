#WAP to input a number and check whether it is a palindrome number or not
n=int(input("Enter a number"))
sum=0
org=n
while n>0:
     r=n%10
     sum=sum*10+r
     n=n//10
if sum==org:
     print('it is palindrome')
else:
     print('It is not palindrome')