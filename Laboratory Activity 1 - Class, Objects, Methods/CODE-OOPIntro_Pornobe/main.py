import Accounts
import ATM

#Initialization
Account1 = Accounts.Accounts(account_number = 123456, account_firstname = "Royce", account_lastname = "Chua", current_balance = 1000, address = "Silver Street Quezon City", email = "roycechua123@gmail.com")
Account2 = Accounts.Accounts(account_number = 654321, account_firstname = "John", account_lastname = "Doe", current_balance = 2000, address = "Gold Street Quezon City", email = "johndoe@yahoo.com")
ATM1 = ATM.ATM(amount = 500, serialNumber = [])
ATM2 = ATM.ATM(amount = 300, serialNumber = [])


#Account1
print("Account 1")

print("First Name: ", Account1.account_firstname)
print("Last Name: ",Account1.account_lastname)
print("Current Balance: ",Account1.current_balance)
print("Address: ",Account1.address)
print("Email: ",Account1.email)
print("Account Number: ", Account1.account_number)
print("Current Balance: ", ATM1.check_currentbalance(Account1))
print("Deposited 500")
ATM1.deposit(Account1, ATM1.amount)
print("New Balance: ", ATM1.check_currentbalance(Account1))

#Outputing a Serial Number
print("SERIAL NUMBER: ", )
ATM1.printSN(ATM1.serialNumber)
print('\n')
#Transaction Summary
print("=========TRANSACTION SUMMARY=========")
ATM1.view_transactionsummary(Account1)

print("\n")


#Account 2
print("Account 2")

print("First Name: ",Account2.account_firstname)
print("Last Name: ",Account2.account_lastname)
print("Current Balance: ",Account2.current_balance)
print("Address: ",Account2.address)
print("Email: ", Account2.email)
print("Account Number: ", Account2.account_number)
print("Current Balance: ", ATM2.check_currentbalance(Account2))
print("Deposited 300")
ATM2.deposit(Account2, ATM2.amount)
print("New Balance: ", ATM2.check_currentbalance(Account2))


#Outputing a Serial Number
print("SERIAL NUMBER: ", )
ATM2.printSN(ATM2.serialNumber)
print('\n')
#Transaction Summary
print("=========TRANSACTION SUMMARY=========")
ATM1.view_transactionsummary(Account2)



