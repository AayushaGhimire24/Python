# 6. Write a python program to add two Distance objects that contain the instance variables km and m.
class Distance:
    def __init__(self,m,km):
        self.m=m
        self.km=km
    def __add__(self,other):
        m=self.m+other.m
        km=self.km+other.km+m//1000
        m=m%1000
        return Distance(m,km)
    
    
d1 = Distance(50, 50)
d2 = Distance(40, 30)

# Adding distances
d3 = d1 + d2
print(d3.km,d3.m)

