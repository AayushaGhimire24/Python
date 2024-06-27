class Student:
    def set(self,name,age,faculty):
        self.__name=name #name is private
        self._age=age #age is protected
        self.faculty=faculty #faculty is public
class ParttimeStudent(Student):
    def show(self):
        #print(self.__name) #error aauxa because private same class ma matra rakhna milxa
        print(self._age)
        print(self.faculty)
s=ParttimeStudent()
s.set('Ram',20,'BIM')
s.show()