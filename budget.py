class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount,"description":description})

    def withdraw(self, amount, description = ""):
        if self.check_funds() >= amount:
            self.ledger.append({"amount": -amount,"description":description})
            return True
        else:
            return False
        
    def transfer(self, amount, category):
        if self.check_funds() >= amount:
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance    


    def check_funds():
        pass