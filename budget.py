class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount,"description":description})

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description":description})
            return True
        else:
            return False
        
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
           
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance
    
    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f'{item["description"][:23].ljust(23)}{format(item["amount"], ".2f").rjust(7)}\n'
            total += item["amount"]
        output = f'{title}{items}Total: {total}'
        return output

def create_spend_chart(categories):
    title = "Percentage spent by category\n"
    names = []
    spent = []
    total = 0
    for category in categories:
        names.append(category.name)
        spent.append(0)
        for item in category.ledger:
            if item["amount"] < 0:
                spent[-1] += item["amount"]
        total += spent[-1]
    for i in range(len(spent)):
        spent[i] = round(spent[i] / total, 2) * 100
    graph = ""
    for i in range(100, -10, -10):
        graph += str(i).rjust(3) + "| "
        for percent in spent:
            if percent >= i:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"
    graph += "    ----" + ("---" * (len(names) - 1))
    graph += "\n     "
    longest_name_length = 0
    for name in names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    for i in range(longest_name_length):
        for name in names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length-1:
            graph += "\n     "
    return (title + graph)


if __name__ == "__main__":
    # Run unit tests automatically
    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())   
    print(food)
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    print(clothing)
    print(create_spend_chart([food, clothing]))