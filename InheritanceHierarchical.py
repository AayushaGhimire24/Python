class Father:
    def fun1(self):
        print('Inside father class')
class Son(Father):
    def fun2(self):
        print('Inside son class')
class Daughter(Father):
    def fun3(self):
        print('Inside daughter class')
s=Son()
s.fun2()
s.fun1()
d=Daughter()
d.fun1()
d.fun3()