#By using format() function
#a)
price=50
txt="Price is {} rupees"
print(txt.format(price))

#b)
item="Noodles"
price=25
txt="Price of {} is {} rupees"
print(txt.format(item,price))

#c)Indexing can be used
item="Noodles"
price=25
txt="{1} is a fast food.Price of {1} is {0} rupees"
print(txt.format(price,item))

#d)We can use named indexing
txt="{item} is a fast food.It costs {price} rupees"
print(txt.format(item="Noodles",price=25))