#WAP to input two numbers,pass them to a function and print all values from first to second number
a=int(input("Enter first number: "))
b=int(input("Enter second number:"))
def numbers(a,b):
    for c in range(a,b+1):
        print(c)
numbers(a,b)