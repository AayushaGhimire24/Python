#create a class Student with the instance variables name,age,faculty.Create a parameterized method set()
#  to set students details and a method show() to
#print student details.Create 2 student objects,set the details and print them.
class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=Student()
s1.set('Abir',20,'IT')
s1.show()
s2=Student()
s2.set('Hope',18,'Mgmt')
s2.show()
