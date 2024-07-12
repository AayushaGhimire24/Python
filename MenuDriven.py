'''Create the following program
1. Write
2.Read
3. Append
Enter your choice'''
while True:
    print("1. Write\n2. Read\n3. Append")
    n = int(input("Enter your choice: "))

    match n:
        case 1:
            with open("menu.txt", "w") as f:
                f.write(input("Enter your writing: "))
        case 2:
            with open("menu.txt", "r") as f:
                print(f.read())
        case 3:
            with open("menu.txt", "a") as f:
                f.write(input("Enter what you want to append: "))
        case _:
            print("Invalid number")
            break


    # how to work in CSV files                 



