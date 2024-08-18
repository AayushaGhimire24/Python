#WAP to input a number and print all of its digits.Also find the sum of all digits
n=int(input("Enter a number: "))
sum=0
while n>0:
    r=n%10
    print(r)
    sum=sum+r
    n=n//10
print(sum)
