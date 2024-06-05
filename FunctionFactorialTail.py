#To inout a number and find ots factorial by using tail recursion
num=1
def fact(n):
    global num
    if n==1:
        num=num*1
    else:
        num=num*n
        fact(n-1)
fact(5)
print(num)
