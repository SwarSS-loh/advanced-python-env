class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
    def balance(self):
        return self.__balance
    def __repr__(self):
        return f"BankAccount(owner={self.__owner}, balance={self.__balance})"
if __name__ == "__main__":
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    try:
        acc.withdraw(300)
    except ValueError as e:
        print(e)
    acc.withdraw(50)
    print(acc.balance())
