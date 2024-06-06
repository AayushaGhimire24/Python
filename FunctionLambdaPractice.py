#From a list of countries,WAP to get only those names that contains the letter 'N'.
coun=['Nepal','China','Canada']
result=filter(lambda a:'N' in a,coun)
print(list(result))