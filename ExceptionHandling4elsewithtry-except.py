#using else with try-except
try:
  a=int(input('Enter first number'))
  b=int(input('Enter second number'))
  c=a/b
  print("result=",c)
except:
  print('Error occured')
else:  
     print('sucessfully completed')