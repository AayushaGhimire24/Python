#WAP to input a sentence and count the numbers of vowels.
count=0
a=input("Enter a sentence: ")
vowels=['a','e','i','o','u']
for x in a:
    if x in vowels:
        count+=1
print("No. of vowels=",count)