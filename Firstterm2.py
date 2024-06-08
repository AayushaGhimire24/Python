#Palindrome or not
# a=int(input("Enter a number"))
# sum=0
# org=a
# while a>0:
#     r=a%10
#     sum=sum*10+r
#     a=a//10
# if sum==org:
#     print("Palindrome")
# else:
#     print("Not palindrome")

#armstrong or not
# a=int(input("Enter a number"))
# sum=0
# org=a
# while a>0:
#     r=a%10
#     sum=sum+r**3
#     a=a//10
# if sum==org:
#  print("Armstrong")
# else:
#    print("Not armstrong")
'''virtual environment is simply a folder(directory) that enables us to create seperate and isolated
 environment for different python projects'''
#python builtin datatypes:
'''numeric(int,flost,complex),string(str),boolean(bool),sequence type(tist,tuple,range),settype(set,frozenset),'''
# a,b=input("Enter 2 words: ").split()
# if len(a)>len(b):
#     print(a,"is longest")
# else:
#     print(b,"is longest")

# count=0
# a=input("Enter a word")
# vowels=['a','e','i','o','u']
# for x in a:
#     if x in vowels:
#     #if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#         count+=1
# print("No. of vowels=",count)

# count=0
# a=input("Enter a word")
# for x in a:
#     vowels=['a','e','i','o','u']
#     if x not in vowels:
#         count+=1
# print("No of consonants",count)
#string slicing->process of extracting a portion of a string
# a='Hello'
# print(a[0:3])
#wap to reverse a string by inputing a word using string slicing
# a=input("Enter a word")
# b=a[-1::-1]
# if a==b: 
#   print("Palindrome")
# else:
#   print("not palindrome")
#string formatting
# age=20
# txt=f"Ram is {age} years old"
# print(txt)
#F string with a function
# a=50.89
# txt=f"rounded value is{round(a)}"
# print(txt)

# #f string with operation
# a=10
# b=20
# txt=f"Addition is {a+b}"
# print(txt)

#using format function
# item="Noodles"
# price=50
# txt="Price of {} is {} rupees"
# print(txt.format(item,price))

# countries=input("Enter the name of 5 countries:").split()
# countries.sort()
# print(countries)

#WAP to input a sentence and count no.of alphabets,digits,space,words
# sentences=input("Enter a sentence: ")
# alpha=0
# digit=0
# space=0
# for ch in sentences:
#   if ch.isalpha():
#     alpha+=1
#   elif ch.isdigit():
#     digit+=1
#   elif ch.isspace():
#     space+=1
# print("Alphabet:",alpha)
# print("Digit:",digit)
# print("Space=",space)
# print("Word:",space+1)
#WAp to input a list of a countries and print them from last to first
# countries=input("Enter the name of a countries: ").split()
# a=countries[::-1]
# print(a)
# mylist=["Apple","Orange","Grapes"]
# mylist[1:4]=["Mango","litchi"]
# print(mylist)

freq=input("Enter a string:")
chars=[]
for ch in freq:
  if ch not in chars:
    chars.append(ch)
for ch in chars:
  print(ch,':',freq.count(ch))