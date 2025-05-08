class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
        print("Account Created..")

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited.")
        print(f"Your balance is {self.get_balance()}")

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credit.")
        print(f"Your balance is {self.get_balance()}")

    def get_balance(self):
        return self.balance


acc1 = Account(1000, 123456789)
print(acc1.balance)
print(acc1.account)

acc1.debit(100)
acc1.credit(500)
