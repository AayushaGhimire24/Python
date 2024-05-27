#WAP to input a name of 5 countries and print only those that ends with a vowel
countries=input("Enter name of 5 countries: ").split()
vowel=('a','e','i','o','u')
for country in countries:
    if country.lower().endswith(vowel):
        print(country)