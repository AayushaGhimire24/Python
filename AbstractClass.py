from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod    
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
c=Circle(3.8)
print('Area is',c.area())
