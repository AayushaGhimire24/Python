#WAP to handle IndexError
countries=['Nepal','India','China','Brazil','Argentina','Portugal']
i=int(input('Enter the index: '))
try:
    print('Country at index',i,'is',countries[i])
except IndexError as ie:
    print(ie)