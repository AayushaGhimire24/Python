#WAP to input name of 5 countries and sort them in ascending order and also in descending order.
countries=input("Enter the name of 5 countries: ").split()
countries.sort()
print("Ascending order: ",countries)


#WAP to input name of 5 countries and sort them in descending order
# countries=input("Enter the name of 5 countries: ").split()
countries.sort(reverse=True)
print("Descending order",countries)