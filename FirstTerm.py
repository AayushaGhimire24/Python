#to inout 2 numbers and perform addition,sub,mul,div
# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=a+b
# d=a-b
# e=a*b
# print("Addition=",c)
# print("Subtraction=",d)
# print("Multiplication=",e)

#input 2 numbers and find sum the square
# a=2
# b=4
# c=a**2+b**2
# print (c)

#WAP to input a number and its square root
# import math as mt
# a=int(input("Enter a number:"))
# b=mt.sqrt(a)
# print("Squareroot= ",b)

'''module is a file that contains different function definitions. some functions inside the math module contains
sqrt(),cbrt(),factorial(),gcd(),lcm(),floor(),ceil()

instead of importing module,we can import all of the  functions'''
# from math import*
# a=int(input("Enter a number:"))
# b=sqrt(a)
# print("Squareroot is=",b)
# import math as mt
# a=int(input("Enter a number:"))
# b=mt.cbrt(a)
# print("Cuberoot is= ",b)

'''the use of asteric* in python is to multiply 2 numbers to import all functions from a module and to repeat the squuence specified number of times'''
# x='hello'*5
# print(x)

#the use of id() function is:it returns memory address of an object
# x=5
# print (id(x))

#type()function is used to return the datatype of a variable
a=5
print(type(a))

#built-in functions are:print(),input(),id(),type(),round(),int(),char(),float(),abs()

'''Indentation means the number of spaces at the beginning of a line of a code
python uses indentation inorder to represent the block of a code
there should be atleast 1 space in the block of a code
,if there is more than one statements in a block,the number of spaces in all statements should be same


python character set:Alphabets:a-z or A-Z digits:0-9 special characters:{},(),[],'',"", >,<,!,:,etc


token:smallest individual unit of code used in a program
types:comment:single line,multiline(helps to increase or improve the code reusability)
whitespace:space,tab,newline
keywords:(Reserved words):words having special characteristics or purpose->try,if,elif,else,for,while,pass,break,etc
punctuators::{},(){}[]"" '' etc
identifier:identifier is a name of a function/array/variable class etc
rules:it can contain alphabets(a-zA-Z) digits(0-9),underscore,it cannot start with a number  it cannot contain blankspace or special characters,keyword cannot be used   python is case sensitive(age and AGE is different)
literals:fixed data items used in aprogram
types of literals:string literals:any texts inside single,double or triple quote
numeric literal:integer,float,complex(a+bi)
boolean literal:true,false
special literal:none
literals collection:list,tuple,dictionary,set
list:collection of values of any datatypes enclosed in a square bracket
tuple:collection of values of any dataypes enclosed on parenthesis
dictionary:unordered collection of data of different types in the form of key:value pairs
set:unordered collection of different types of data enclosed inside curly bracket
operators:arithmetic(+*-/%///**),logical(and or not) relational(>,<,>=,<=,==,!=),assignment(=,+=,-=),membership(in,not in),identity(is,is not),bitwise(&,|,^,~,>>,<<)'''

'''PIP is a default program installer in python that stands for preferred installer program,it is used to install or uninstall preferred third party libraries in python
to install:pip install numpy'''

'''the process of extracting values of a sequence and assigning them to different variables is called unpacking'''
# a,b,c=input("Enter the numbers").split(',')
# x=int(a)
# y=int(b)
# z=int(c)
# d=x+y+z
# print("sum=",d)

# x=["KTM","Bkt","PKR"]
# a,b,c=x
# print(a)
# print(b)
# print(c)

'''if types:if->checks onlu one condition;if else->checks 2 conditions;if elif else->checks more than 2 conditions;nested if->if inside if'''
'''if condition1:
    statements
   elif condition2:
     statements
   else:
     statements
nested if:
if condition:
    if condition 
       statements
    else:
        statements
else:
    statements'''
#odd even
# a=int(input("Enter a number:"))
# if a%2==0:
#     print('even')
# else:
#     print("odd")

#positive,negative,zero
# x=int(input("Enter a number"))
# if x<0:
#     print("Negative")
# elif x>0:
#     print("Positive")
# else:
#     print("Zero")

#input 2 numbers and print the smaller one
# a,b=(input("Enter2  numbers:")).split(',')
# x=int(a)
# y=int(b)
# if x<y:
#     print("Smaller=",x)
# else:
#     print("Smaller=",y)

# input 3 numbers and print the middle Value
# x,y,z=input("Enter 3 numbers").split(',')
# a=int(x)
# b=int(y)
# c=int(z)
# if a<b and a>c:
#     print("Middle number=",a)
# elif b>a and b<c:
#     print("millde number",b)
# else:
#     print("Middle number=",c)


#print its factorial only if it is less than 10
# import math as mt
# x=int(input("Enter a number"))
# if x<10:
#     print(mt.factorial(x))
# import math as mt
# x=int(input("Enter a number"))
# if x<10:
#     print(mt.factorial(x))
#using nested-if
'''WAP to input marks in 3 subjects and calculate total marks,percentage,result(pass/fail) and division'''
# a=int(input("Enter 1st subject"))
# b=int(input("Enter 2nd subject"))
# c=int(input("Enter 3rd subject"))
# t=a+b+c
# p=t/3
# print("Total marks=",t)
# print("Percentage=",round(p,2))
# if a>=50 and b>=50 and c>=50:
#     print ("Pass")
#     if p>=80:
#         print("Distinction")
#     elif p>=70:
#         print("First division")
#     else:
#         print("Second division")
# else:
#     print("Fail")

#match case:
'''match expression:
      case value1:
          statement
      case value2:
           statement
      case other:
           statement'''
#WAP to input the day number and print the respective day
# day=int(input("Enter a number"))
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case other:
#         print("Invalid")

# using | in case statement
#Input a letter and check vowel consonant
# letter=input("Enter a letter")
# letter=letter.lower()
# match letter:
#     case'a'|'e'|'i'|'o'|'u':
#         print("vowel")
#     case other:
#         print ("consonant")

# x=input("Enter a letter")
# x=x.lower()
# match x:
#     case 'a'|'e'|'i'|'o'|'u':
#         print("vowel")
#     case other:
#         print("Consonant")

# create the following menu driven program:add sub mul div
# print('1,Add\n 2.Subtract\n 3.Multiply\n 4.Divide')
# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# choice=int(input("Enter your choice(1-4)"))
# match choice:
#     case 1:
#         c=a+b
#         print("Result",c)
    # case 2:
    #     c=a-b
    #     print("Result=",c)
    # case 3:
    #     c=a*b
    #     print("Result=",c)
    # case 4:
    #     c=a/b
    #     print("Result=",c)
    # case others:
    #     print("invalid")
    #ternary operator syntax={result_if_true if condition else result_if_false}
# a="Even" if 4%2==0 else "odd"
# print(a)
#input a number and check odd/even using if else as ternary operator
# a=int(input("Enter a number"))
# msg="Even" if a%2==0 else "Odd"
# print(msg)


#WAP to input 2 numbers and print the greater number using if else as ternary operator
# a=int(input("Enter 1st number: "))
# b=int(input("Enter 2nd number: "))
# grt=a if a>b else b
# print(grt)

#Nested ternary operator
# msg="divisible by 5" if 20%5==0 else "Even" if 5%2==0 else "odd"
# print(msg)

#using if else ternary operator,WAP to input 3 numbers and print the smallest number
# a,b,c=input("Enter 3 numbers: ").split()
# x=int(a)
# y=int(b)
# z=int(c)
# msg=x if x<y and x<z else y if y<x and y<z else z
# print(msg)

#Loop in python
#for loop while loop
#for loop->it is used to iterate over the items in a sequence(list,tuple,range)
# fruits=["Apple","Orange","mango"]
# for x in fruits:
#     print(x)
# fruit='APPLE'
# for x in fruit:
#     print(x)

#Using for loop with range() function
# for x in range(1,6):
#     print(x)
# for x in range(1,6,2):
#     print(x)
# for x in range(1,51):
#     print(x,end=' ')
# for x in range(50,0,-2):
#     print(x ,end=' ')
# for x in range(5,101,5):
#       print(x,end=' ')

#sum of 50 natural numbers
# sum=0
# for x in range(1,51):
#     sum=sum+x
#     print("Sum=",sum,end=' ')

# n=int(input("Enter a number"))
# sum=0
# for x in range(1,n+1):
#     sum=sum+x
# print(sum)
#Factorial

# n=int(input("Enter a number: "))
# factorial=1
# for x in range(1,n+1):
#     factorial=factorial*x
# print(factorial)

# n=int(input("Enter a number"))
# count=0
# for x in range(1,n+1):
#   if n%x==0:
#       count+=0
# if count==2:
#    print("prime")
# else:
#    print("Composite")

#Prime numbers between  100 to 200
# for n in range(99,201):
#   count=0
#   for x in range(1,n+1):
#     if n%x==0:
#       count+=1
#   if count==2:
#     print(n,end=' ')

#using brreak and continue
# break is used inside the loop to terminate the loop if specified condition matches
#continue is used inside the loop to continue with the next iteration if specified condition matches
# x=[1,2,3,4,5]
# for a in x:
#     if a==3:
#         break
#     print(a)

#using else in for loop
'''else can be used in a loop to identify whether the loop completed execution successfully or it was
 forcefully terminated by the break statement'''
# w='NEPAL'
# for i in range(0,5):
#     for j in range(0,i+1):
#        print(w[j],end=' ')
#     print()
# sp=1
# W='KATHMANDU'
# for i in range(8,-1,-2):
#     for k in range(1,sp+1):
#       print(end=' ')
#     for j in range(0,i+1):
#       print(W[j],end='')
#     print()
#     sp=sp+1
# i=1
# while i<=50:
#     print(i,end=' ')
#     i+=1
# i=1
# while i<50:
#     if i%2!=0: 
#         print(i,end=' ')
#     i+=1
# i=5
# while i<=100:
#     if i%5==0:
#      print(i,end=' ')
#     i+=1
# i=5
# a=5
# d=5
# while i<=10:
#    print(a,end=' ')
#    a=a+i
#    d=d+5
#    i=i+1
#to input a number and count the number of digits
# n=int(input("Enter a number"))
# count=0
# while n>0:
#     count+=1
#     n=n//1
# print("No. of digits=",count)
#good bad number
# n=int(input("Enter a number"))
# c0=0
# c1=0
# while n>0:
#     r=n%10
#     if r==0:
#         c0+=1
#     elif r==1:
#         c1+=1
#     n=n//10
# if c0==c1:
#   print("Good number")
# else:
#     print("Bad number")
#WAP to input a number and find it's reverse
n=int(input("Enter a number"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
print("The number is sum",rev)