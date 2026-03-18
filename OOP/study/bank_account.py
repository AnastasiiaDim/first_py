class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance #Private attribute (double underscore) - Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

account_1 = BankAccount("", 100)
account_1.deposit(10)
account_1.withdraw(5)
print(account_1.get_balance())
