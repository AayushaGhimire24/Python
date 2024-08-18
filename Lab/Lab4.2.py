# Create a function that takes list of 5 country names and return only those countries that start with N.
def starts(countries):
    a = []
    for country in countries:
        if country.lower().startswith('n'):
            a.append(country)
    return a

countries = ['Nepal','USA', 'Germany', 'Nigeria', 'Iraq']
print(starts(countries))
