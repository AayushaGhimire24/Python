#Create a function that takes a list of country names and return the countries that ends with vowel
def vowel(countries):
    vowel=('a','e','i','o','u')
    a=[]
    for country in countries:
        if country.lower().endswith(vowel):
            a.append(country)
    return a
countries=['USA','Germany','India','Iraq','Pakistani']
print(vowel(countries))