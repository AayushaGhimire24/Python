def find_mod(dividend,divisor):
    modulus=dividend%divisor
    return modulus

dividend=int(input("Enter Dividend "))
divisor=int(input("Enter Divisor"))
result=find_mod(dividend,divisor)
print(result)