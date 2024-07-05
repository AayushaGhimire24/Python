try:
 a=int(input("Enter first number: "))
 b=int(input("Enter second number: "))
 c=a/b
 print("Result= ",c)
# except ValueError as ve:
#   print(ve)
# except ZeroDivisionError as ze:
#   print(ze)

  #Custom handling
  #Handling Multiple Exceptions with a single except block
# except (ValueError,ZeroDivisionError) as e:
#   print(e)

  #Alternative
except:
  print("Error occured")