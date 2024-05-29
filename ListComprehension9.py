mylist=["a","b","c","d","e"]
newlist=[x for x in mylist]
print(newlist)

#From existing list of item,make a list which doesnot includes "a" using list comprehension
#yo chai without list comprehension
fruits=["Apple","mango","cherry","litchi"]
newlist=[]
for x in fruits:
    if 'a' not in x:
        newlist.append(x)
print(newlist)

#yo with list comprehension
fruits=["Apple","mango","cherry","litchi"]
newlist=[x for x in fruits if 'a' not in x]
print(newlist)