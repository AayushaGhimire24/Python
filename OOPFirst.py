#first class and object program
class Student:
    def config(self):#config() vaneko instance method or method
          self.name='Ram'
          self.age=20 #name and age are instance variables or attributes


#object banaune
s1=Student()
s1.config()
print(s1.name,s1.age)
