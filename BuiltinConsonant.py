#WAP to input a word and count the no. of consonants
count=0
a=input("Enter a word: ")
vowels=['a','e','i','o','u']
for x in a:
   if x not in vowels:
      count+=1
print("No. of consonant=",count)    