#WAP to input a sentence and count the frequency of all the characters
freq=input("Enter a sentence: ")
chars=[]
for ch  in freq:
    if ch not in chars:
        chars.append(ch)
for ch in chars:
    print(ch,':',freq.count(ch))
