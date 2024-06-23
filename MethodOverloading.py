from multipledispatch import dispatch 
class Student:
    @dispatch(str,int)
    def set(self,name,age):
        self.name=name
        self.age=age
    @dispatch()
    def set(self):
        self.name='Hari'
        self.age=20
    def show(self):
        print(self.name,self.age)
s1=Student()
s1.set('Ram',20)
s1.show()
s2=Student()
s2.set()
s2.show() 