#WAP to inout a string and count the frequency of all characters
freq=input("Enter a string: ")
chars=[]
for ch  in freq:
    if ch not in chars:
        chars.append(ch)
for ch in chars:
    print(ch,':',freq.count(ch))
