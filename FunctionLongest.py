#Create a function that takes a list of country names and return the longest country name
def longest(country):
    long=country[0]
    for i in range(1,len(country)):
        if len(country[i])>len(long):
            long=country[i]
    return long
country=['Nepal','Canada','United States of America']
print(longest(country))
