#create a class Student with the instance variables name,age,faculty.Create a parameterized method set()
#  to set students details and a method show() to
#print student details.Create 5 student objects,and print only those records who study BIM.
class Student:
    def set(self,name,age,faculty):
        self.name=name
        self.age=age
        self.faculty=faculty
    def show(self):
        print(self.name,self.age,self.faculty)
s1=Student()
s1.set('Abir',20,'BIT')
s2=Student()
s2.set('Hope',18,'BIM')
s3=Student()
s3.set('Harry',11,'BCA')
s4=Student()
s4.set('Hina',20,'BIM')
s5=Student()
s5.set('Ian',22,'BIM')
students=[s1,s2,s3,s4,s5]
for std in students:
    if std.faculty=='BIM':
        std.show()


