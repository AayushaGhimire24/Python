#WAP to input a sentence and count no.of alphabets,digits,space,words
sentences=input("Enter a sentence: ")
alpha=0
digit=0
space=0
for ch in sentences:
    if ch.isalpha():
        alpha+=1
    if ch.isdigit():
        digit+=1
    if ch.isspace():
        space+=1
print('Alphabet',alpha)
print('Digits',digit)
print('Space',space)
print('word',space+1)





