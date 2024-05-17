#To find sum of first N natural numbers
n=int(input('enter a number'))
sum=0
for x in range(1,n+1):
    sum=sum+x
print("The sum is:",sum)