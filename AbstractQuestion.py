#Create an abstract class
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def makesound(self):
        pass

class Dog(Animal):
    def makesound(self):
        print('woff woff')

class Cat(Animal):
    def makesound(self):
        print('Meow')

d=Dog()
d.makesound()
c=Cat()
c.makesound()
