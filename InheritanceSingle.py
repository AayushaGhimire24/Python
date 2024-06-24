#single inheritance
class Person:
    def setP(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
class Student(Person):
    def setS(self,faculty):
         self.faculty=faculty
    def show (self):
        super().show()
        print(self.faculty)
s1=Student()
s1.setP('Ram',20)
s1.setS('BIM')
s1.show()