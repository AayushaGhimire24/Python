#eg:1
'''
a='Hello'
b=a[0:3]
print(b)'''

#eg:2
'''
a='Hello'
b=a[1:4]
print(b)'''

#eg:3
'''
a='Hello'
b=a[1:]
print(b)'''

#eg:4
'''
a='Hello'
b=a[:3]
print(b)'''

#eg:5
'''
a='Hello'
b=a[:]
print(b)'''

#eg:6
'''
a='Hello World'
b=a[::]
print(b)'''

#eg:7
'''
a='Hello'
b=a[-5:-2]
print(b)'''

#eg:8
#WAP to input a word and reverse it using string slicing
'''
a=input("Enter a word ")
b=a[-1::-1]
print(b)'''


#WAP to input a word and check whether it is palindrome or not
a=input("Enter a word ")
b=a[-1::-1]
if a==b:
    print("Palindrome")
else:
    print("Not Palindrome")
