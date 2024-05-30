city=['Bkt','ktm','pkr','brt']
# city.sort()#case sensitive
#to reduce case sensitivity:
city.sort(key=str.lower)
print (city)