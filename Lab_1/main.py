"""import sys
class BankAccount:
    def __init__(self, pin, balance, inrate, serviceCharge = 5, depot_num = 0, withdraw_num = 0):
        self.pin = pin
        self.balance = balance
        self.inrate = inrate
        self.serviceCharge = serviceCharge
        self.depot_num = depot_num
        self.withdraw_num = withdraw_num

    def __closed__(self):
        return "The transaction has been completed. Exiting the account"
        sys.exit()

    def deposits(self, deposit):
        balance = self.balance + deposit
        self.balance = balance
        self.depot_num = self.depot_num + 1
        return self.balance

    def withdraw(self, withdraw):
        balance = self.balance - withdraw
        self.balance = balance
        self.withdraw_num = self.withdraw_num + 1
        return self.balance

    def calc_interest(self):
        monIntrate = self.inrate / 12
        monInt = self.balance * monIntrate
        self.balance = self.balance + monInt
        return self.balance

    def monthly_process(self):
        self.balance = self.balance - self.serviceCharge
        self.calc_interest()
        self.depositNum = 0
        self.withdrawNum = 0

##OBJECTS:
bank_account = BankAccount(8521, 1000, .02)

##Calling the methods

val_1 = input("How many deposits are you making? ")

while int(val_1) > 0:
    val_usr = input("Type your Deposit: ")
    try:
        if int(val_usr) < 0:
            print("Invalid Deposit. Please enter a valid deposit")
        else:
            print("Balance = " + str(bank_account.deposits(int(val_usr))))
            val_1 = int(val_1) - 1
    except ValueError:
        print("Invalid Deposit. Please enter a valid deposit")


val_2 = input("How many withdraws are you making? ")

while int(val_2) > 0:
    val_usr2 = input("Type your withdrawl: ")
    try:
        if int(val_usr2) < 0 or int(val_usr2) >= bank_account.balance:
            print("Invalid Withdraw. Please enter a valid withdraw")
        else:
            print("Balance = " + str(bank_account.withdraw(int(val_usr2))))
            val_2 = int(val_2) - 1
    except ValueError:
        print("Invalid Deposit. Please enter a valid deposit")


bank_account.monthly_process()
print("Balance: " + "{:.2f}".format(bank_account.balance))

print(bank_account.__closed__())"""
'''
def func(x):
    res = 0
    for i in range(x):
        res += i
    return res

print(func(4))

n = 5
for i in range(n):
    print(i + 1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(7))
print(factorial(5))
print(factorial(2))
print(factorial(5))

def sum_of_sequence(m):
    if m == 0:
        return 0
    else:
        return m + sum_of_sequence(m-1)

print(sum_of_sequence(5))

def fibonnaci(s):
    if s <= 1:
        return s
    else:
        return (fibonnaci(s-1) + fibonnaci(s-2))

print(fibonnaci(6))
'''
