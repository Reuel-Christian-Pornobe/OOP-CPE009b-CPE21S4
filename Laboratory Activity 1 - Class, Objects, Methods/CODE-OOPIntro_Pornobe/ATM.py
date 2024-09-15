import random


class ATM():
    
    def __init__(self, amount, serialNumber):
        self.amount = amount
        self.serialNumber = serialNumber
        self.reportW = 0
        self.reportD = 0
        self.balance0 = 0
        self.balance1 = 0
        
    def deposit(self, account, amount):
        self.balance0 = account.current_balance
        account.current_balance = account.current_balance + self.amount
        self.reportD = self.amount
        self.balance1 = account.current_balance
        print("Deposit Complete")
        
    def withdraw(self, account, amount):
        self.balance0 = account.current_balance
        account.current_balance = account.current_balance - self.amount
        self.reportW = self.amount
        self.balance1 = account.current_balance
        print("Withdraw Complete")
        
    def check_currentbalance(self, account):
        return account.current_balance
        
    def printSN(self, serialNumber):
        
        for i in range(1, 10):
            self.serialNumber.append(random.randint(0,9))
            
        for i in self.serialNumber:
            print(i, end="")
        
    def view_transactionsummary(self,account):    
        
        if self.reportD >> 0:
            print("Old Balance: ", self.balance0)
            print("Money Deposited in Account Number ", account.account_number, " is ", self.reportD)
            print("New Balance: ", self.balance1)
        elif self.reportW >> 0:
            print("Old Balance: ", self.balance0)
            print("Money Withdrawn in Account Number ", account.account_number, " is ", self.reportW)
            print("New Balance: ", self.balance1)
    
        
        
        