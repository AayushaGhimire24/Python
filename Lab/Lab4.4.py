#Write a program to find factorial of a number using recursive function.
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
