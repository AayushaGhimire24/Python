#WAP to input a number and find its factorial
n=int(input('enter a number'))
factorial=1
for x in range(1,n+1):
    factorial=factorial*x
print("The factorial is:",factorial)