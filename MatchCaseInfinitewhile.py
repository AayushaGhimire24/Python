""" Create the following menu driven program using while true(infinite):
 1.Add
 2.Subtract
 3.Multiply
 4.Divide
 5.Exit"""
while True:
 print('1.Add\n2.Subtract\n3.Multiply\n4.Divide')
 a=int(input('enter first number'))
 b=int(input('enter second number'))
 choice=int(input('Enter your choice(1-5):'))
 match choice:
    case 1:
        c=a+b
        print("Result=",c)
    case 2:
        c=a-b
        print("Result=",c)
    case 3:
        c=a*b
        print("Result=",c)
    case 4:
        c=a/b
        print("Result=",c)
    case 5:
        break
    case other:
        print("invalid choice")