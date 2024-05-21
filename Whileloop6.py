#WAP to input a number and count number of digits
n=int(input("Enter a number"))
count=0
while n>0:
    count+=1
    n=n//10 #// is integer division,so float number input dina paudaina
print('No. of digits=',count)