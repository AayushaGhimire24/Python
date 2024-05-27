#WAP to input name of 5 countries & print only those names that begin with "N"
countries=input("Enter name of 5 countries: ").split()
for country in countries:
    if country.lower().startswith('n'):
        print(country)