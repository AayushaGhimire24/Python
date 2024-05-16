#WAP to input a day number and print respective day name
day=int(input('Enter day number'))
match day:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednusday')
    case 5:
        print('thrusday')
    case 6:
        print('friday')
    case 7:
        print('saturday')
    case _:
        print('Invalid day')
    
    