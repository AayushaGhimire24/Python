'''WAP to overload + and - operators to add and subtract two Distance objects that contain the instance
 variables km and m'''
class Distance:
    def __init__(self,m,km):
        self.m=m
        self.km=km
    def __add__(self,other):
        m=self.m+other.m
        km=self.km+other.km+m//1000
        m=m%1000
        return Distance(km,m)
    
    def __sub__(self,other):
        m=self.m-other.m
        km=self.m-other.km
        return Distance(km,m)
    
d1 = Distance(50, 50)
d2 = Distance(40, 30)

# Adding distances
d3 = d1 + d2
print(d3.km,d3.m)

# Subtracting distances
d4 = d1 - d2
print(d4.km,d4.m)

        