#Methods with parameters
class Student:
    def config(self,name,age):
        self.name=name
        self.age=age
    def print(self):
        print(self.name,self.age)
s1=Student()
s1.config("Ram",20)
s1.print()
s2=Student()
s2.config("Hari",40)
s2.print()