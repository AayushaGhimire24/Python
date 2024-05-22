#WAP to  input two words and print the longest word.
a,b=input("enter two words ").split()
if len(a)>len(b):
    print(a,"is longest")
else:
    print(b,"is longest")