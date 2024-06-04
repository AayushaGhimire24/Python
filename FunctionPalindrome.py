#Create a function check() that takes a word as argument and check paindrome or  not
def palin(n):
    sum=0
    org=n
    while n>0:
     r=n%10
     sum=sum*10+r
     n=n//10
    if sum==org:
         print("Palindrome") 
    else:
       print("not palindrome")
palin(102)