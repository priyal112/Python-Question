# Create a class BankAccount with methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

# Test
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(300)
print("Final Balance:", acc.get_balance())
