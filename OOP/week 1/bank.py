class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return ("Minimum withdraw is 100")
        elif amount > self.max_withdraw:
            return ("Maximum withdraw is 10000")
        elif amount > self.balance:
            return (f'Insufficient Balance. Your balance is {self.balance}')
        else:
            self.balance -= amount
            return (
                f'Withdrawn {amount} and remaining balance is {self.balance}')

    def deposit(self, amount):
        self.balance += amount


customer1 = Bank(8000)
reply = customer1.withdraw(555)
print(reply)
customer1.deposit(5055)
print(customer1.get_balance())
