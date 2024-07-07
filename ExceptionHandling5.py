#printing the detail exception message
import traceback
try:
  a=int(input('Enter first number'))
  b=int(input('Enter second number'))
  c=a/b
  print("result=",c)
except ZeroDivisionError as e:
  print(traceback.format_exc())