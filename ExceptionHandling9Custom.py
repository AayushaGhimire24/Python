'''Create ypur exception class 'AgeError' that is raised when age is less than 18 and check whether the
 person can vote or not'''
class AgeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
age=int(input("Enter your age"))
try:
    if age<18:
        raise AgeError('Not capable of voting')
    else:
        print("Capable of voting")
except AgeError as ie:
    print(ie)