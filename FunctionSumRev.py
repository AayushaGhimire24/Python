#Create a function that takes two numbers a and b and return the sum of a and reverse value of b.{Eg:5 12 =5+21=26}
def sum_rev(a,b):
    rev=0
    while b>0:
        v=b % 10
        rev=rev*10+v
        b=b//10
    return rev+a
print(sum_rev(5,12))