#WAP to input a sentence and count its numbers of characters
sentence=input("Enter a sentence: ")
space=0
for ch in sentence:
    if ch.isspace():
        space+=1
print("Character=",space+1)