#to sort name of cities without using sort() method
cities=input("enter the name of the cities: ").split()
for i in range(0,5):
    for j in range(i+1, 5):
        if(cities[i]>cities[j]):
            temp=cities[i]
            cities[i]=cities[j]
            cities[j]=temp
print(cities)
    