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


class Bank_account:
    #constuctor
    def __init__(self, mybalance, account):
        self.balance = mybalance
        self.accountNum = account

    def set_balance(self, mybalance):
        self.balance = mybalance

    def set_account_number(self, account):
        self.accountNum = account

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNum

    

    
# child one
class Saving_account(Bank_account):
    # constructor
    def __init__(self, mybalance, account, interest = 0.05):
        super().__init__(mybalance, account)
        self.interested = interest

# child two
class Checking_account(Bank_account):
    # constructor
    def __init__(self, mybalance, account, gifts):
        super().__init__(mybalance, account)
        self.somegifts = gifts

class Customer:
    pass
