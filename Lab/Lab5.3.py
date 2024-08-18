# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
import math as mt
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 2*3.14*self.radius
    
class Triangle(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return(mt.sqrt(3) / 4) * (self.length ** 2)
    def perimeter(self):
        return 3 * self.length
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
    def perimeter(self):
        return 4*self.length
    
circle = Circle(10)
square = Square(5)
triangle = Triangle(6)

print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
print(f"Triangle - Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter()}")   
print(f"Square - Area: {square.area()}, Perimeter: {square.perimeter()}")
