#Write a program to handle ZeroDivisionError
#Custom generated
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
try:
    c=a/b
    print("Result= ",c)
# except ZeroDivisionError:
#     print("Attempt to divide by zero.")


    #Printing system generated exception message
except ZeroDivisionError as ze:
    print(ze)