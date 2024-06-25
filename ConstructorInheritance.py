#using constructor inheritance:-
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def __init__(self,name,age,faculty):
        super().__init__(name,age)
        self.faculty=faculty
    def show(self):
        super().show()
        print(self.faculty)
        print(self.name,self.age,self.faculty)
s=Student('Ram',20,'BIM')
s.show()