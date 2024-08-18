#Create a function that takes radius of circle as input from user and return the area
def circle(r):
    return 3.14*r**2
area=int(input("Enter area of a circle: "))
a=circle(area)
print(a)