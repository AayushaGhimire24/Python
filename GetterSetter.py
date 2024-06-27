'''Create a class Car with the private instance variables model and price.Create getters ans setters.
 Create a car object,set the details and print them'''

class Car:
    def set_model(self,model):
        self.__model=model
    @property
    def get_model(self):
        return self.__model
    
    def set_price(self,price):
        self.__price=price
    @property
    def get_price(self):
        return self.__price
c=Car()
c.set_model('Nexon')
c.set_price(200000)
print(c.get_model(),c.get_price())

