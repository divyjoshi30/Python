class Account:
    """ Simple account class with balance  Part 1"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))


if __name__ == '__main__':
    dj = Account("DIVY", 0)
    dj.show_balance()

    dj.deposit(10000)
    # dj.show_balance()
    dj.withdraw(2500)
    # dj.show_balance()

    dj.withdraw(2000)

'''Methds part 1 finished '''

''' Methods part 2 upcoming '''