class Car:
    def set_model(self,model):
        self.__model=model
    def get_model(self):
        return self.__model
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price
    Model=property(get_model,set_model) 
    Price=property(get_price,set_price)
c=Car()
c.Model="Scorpio" #calls set_model
c.Price=150 #calls set_price
print(c.Model,c.Price)#calls get_model and get_price