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

jack = Bank(5000)
jack.showBalance()
jack.depositMoney(5000)
jack.withdrawMoney(100000)
jack.withdrawMoney(3000)