'''Create an abstract classAnimal with one abstract method makesound().
Create the derived classes Dog,Cat from Animal,Instantiate them and call makesound()'''
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
