from multipledispatch import dispatch
class Student:
    @dispatch()
    def __init__(self): #default constructor
        self.name='Ram'
        self.age=20
    @dispatch(str,int)
    def __init__(self,name,age): #parameterized constructor
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
s1=Student()
s1.show()
s2=Student('Hari',21)
s2.show()