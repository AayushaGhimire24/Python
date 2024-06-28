''' Using property decorator'''
class Car:
    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,model):
        self.__model=model
        
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,price):
        self.__price=price
    
c=Car()
c.Model="Scorpio" #calls set_model
c.Price=150 #calls set_price
print(c.Model,c.Price)#calls get_model and get_price

      
