# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if(b==0):
            print("Error division")
        return a/b
calc=Calculator()
a=int(input("Enter Num1:"))
b=int(input("Enter Num2:"))
print(f"Addition is:{calc.add(a,b)}")
print(f"Subtraction is:{calc.sub(a,b)}")
print(f"Multiplication is:{calc.mul(a,b)}")
print(f"Division is:{calc.div(a,b)}")
    