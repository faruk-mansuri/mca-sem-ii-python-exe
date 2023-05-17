class Bank:
    def __init__(self, amount):
        self.money = amount

    def depositMoney(self, amount):
        self.money+=amount
        print(f"available balance is: {self.money}")
    
    def withdrawMoney(self, amount):
        if self.money < amount:
            print(f"withdrawal amount is greater than deposited money ")
            return
        self.money-=amount
        return self.showBalance()
    
    def showBalance(self):
        print(f"current balance is {self.money}")

# jack = Bank(5000)
# jack.showBalance()
# jack.depositMoney(5000)
# jack.withdrawMoney(100000)
# jack.withdrawMoney(3000)

def Bank(name, amount):
    name = name
    amount = amount

    def display_amount():
        return f"available balance is: {amount}"

    def deposite(deposite_amount):
        nonlocal amount
        amount += deposite_amount
        return display_amount()

    def withdraw_amount(withraw_amount):
        nonlocal amount
        if withraw_amount > amount:
            return f"sorry can not do this transaction! your available balance is {amount}"

        amount -= withraw_amount
        return withraw_amount

    return {"display_amount":display_amount, "deposite":deposite, "withdraw_amount":withdraw_amount}

jack = Bank("Jack", 5000)
print(jack["display_amount"]())
print(jack["deposite"](3000))
print(jack["withdraw_amount"](3000))
print(jack["display_amount"]())



