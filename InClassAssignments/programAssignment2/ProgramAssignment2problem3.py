# Paxton Proctor
# Programassignment2
# Problem 3
# CMPS-4143-101 Top: Cont Programming Language
# 11/8/2021
# (30 points) Write the OOP program in python using class. Assuming you have four
# classes: Bank account which is the parent class and it has two child classes Saving
# Account class and Checking account class. Customer is another class who has a bank
# account; either saving or checking or both. Implement the scenario using python OOP
# and make sure you have covered those OOP concepts on your code: inheritance(any),
# polymorphism (runtime and compile time), abstraction and encapsulation.


class Bank_account():
    #constuctor
    def __init__(self, mybalance, account):
        self.balance = mybalance
        self.accountNum = account

    #setters
    def set_balance(self, mybalance):
        self.balance = mybalance

    def set_account_number(self, account):
        self.accountNum = account

    #getters
    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNum

    def show_balance(self):
        print("Here is your balance: ", self.balance)

    # depositing money into account
    def Deposit(self, money):
        self.balance += money
        print("You deposited this amount: ", self.money, " Here is your new balance: ", self.balance)
    

    #abstraction and withrawing money into account
    def Withdraw(self, money):
        self.balance -= money
        print("You withdrew this amount: ", self.money, " Here is your new balance: ", self.balance)

       

    
# child one
class Saving_account(Bank_account):
    # constructor
    def __init__(self, mybalance, account, interest = 0.05):
        super().__init__(mybalance, account)
        self.interested = interest
    
    def show_savings(self):
        print("Savings")
        self.show_balance()
        self.show_interest()

    def show_interest(self):
        print("your balance with interest: ", self.interested*self.get_balance()/100)

# child two
class Checking_account(Bank_account):
    # constructor
    def __init__(self, mybalance, account, gifts = 20):
        super().__init__(mybalance, account)
        self.somegifts = gifts

    def show_checkings(self):
        print("Checkings")
        self.show_balance()
        self.show_gifts()

    def show_gifts(self):
        print("your balance with gifts: ", self.somegifts+self.get_balance())
    
class Customer(Saving_account, Bank_account):
    def __init__(self, mybalance, account, account_type):
        self.accounter = account_type
    
    def show_account_type(self):
        if(self.accounter == 's'):
            Saving_account.__init__(self, mybalance, account, interest = 0.05)
            Saving_account.show_savings(self)

        if(self.accounter == 'c'):
            Checking_account.__init__(self, mybalance, account, gifts = 20)
            Checking_account.show_checkings(self)

a = input("Enter C or S to open a account ")
mybalance = int(input("Enter your amount of money you want into the bank "))
account = int(input("Enter your account number "))
customer = Customer(mybalance, account, a)

