#WAP to input 2 words and print the longest word.
a=input("Enter the first word: ")
b=input("Enter the second word: ")
if len(a)>len(b):
    print(a,"is longest")
elif len(b)>len(a):
    print(b, "is longest")
else:
    print("Both are of equal length.")
