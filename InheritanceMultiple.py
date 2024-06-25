class Father:
    def fun1(self):
        print('Inside Father class')
class Mother:
    def fun2(self):
        print('Inside Mother class')
class Son(Father,Mother):
    def fun3(self):
        print('Inside Son class')
s=Son()
s.fun1()
s.fun2()
s.fun3()
