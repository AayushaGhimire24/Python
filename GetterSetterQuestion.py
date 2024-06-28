'''Create a class Car with the private instance variables model,price and provide getters and setters.
 Create N Car objects, set their details and print only those cars whose price is less than 2500000'''
class Car:
    def set_model(self,model):
        self.__model=model
    def get_model(self):
        return self.__model
    
    def set_price(self,price):
        self.__price=price
    def get_price(self):
        return self.__price

n=int(input("Enter the number of cars: "))
cars=[]
for x in range(n):
 c=Car()
model=int(input("Enter model"))
price=int(input('Enter price'))
c.set_model(model)
c.set_price(price)
cars.append(c)
for c in cars:
    if c.get_price()<2500000:
        print(c.get_model(),c.get_price())
