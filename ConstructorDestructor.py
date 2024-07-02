class Employee:
    def __init__(self):
        print("Constructor called")
    def __del__(self):
        print("Destructor called")
e=Employee()
del e