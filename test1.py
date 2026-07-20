"""
Write a class Wallet with a private __balance (start at 0). 
Add a public method get_balance() that returns it, and add_money(amount) that increases it. 
Then write a class Person that HAS-A Wallet (composition — store it as self.wallet). 
Give Person a method check_money() that calls self.wallet.get_balance() and prints it.
"""

class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def increase_amount(self, amount):
        initial_balance = self.__balance
        self.__balance = self.__balance + amount
        print(f"Balance increased from {initial_balance} to  : {self.__balance}")
        
class Person:
    def __init__(self, wallet):
        self.wallet = wallet

    def add_money(self, amount):
        self.wallet.increase_amount(amount)

    def check_money(self):
        print(f"Current Balance: {self.wallet.get_balance()}")       

w = Wallet(1000)
p1 = Person(w)
p1.add_money(900)     
p1.check_money()     


