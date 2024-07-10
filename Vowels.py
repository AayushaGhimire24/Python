# WAP to count no.of vowels characters in a file
count=0
text=open("abc.txt","r")
text=text.read()
vowel=['a','e','i','o','u']
for x in text:
    if x in vowel:
        count+=1
print (count)
print(len(text))