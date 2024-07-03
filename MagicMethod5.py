'''WAP to overload < operator to check(compare) two Person objects which contain the instance variables name and age'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __lt__(self,other):
        return self.age<other.age

p1=Person('Ram',20)
p2=Person('Hari',21)
if p1<p2:
    print(p1.name,p1.age)
else:
    print(p2.name,p2.age)