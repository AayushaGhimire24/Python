#Creating custom(user defined) exception/error class:
class InsufficientBalanceError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
balance=int(input("Enter balance amount"))
amount=int(input("Enter withdraw amount"))
try:
    if amount>balance:
        raise InsufficientBalanceError('Balance Not Enough')
    else:
        balance=balance-amount
        print('Withdraw Successful')
        print('Withdraw amount=',amount)
        print('Balance after withdraw=',balance)
except  InsufficientBalanceError as ie:
    print(ie)