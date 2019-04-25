''' Methods Part 2 begins '''
print("Methods Part 2 begins")

import datetime
import pytz

class Account:
    """ Simple account class with balance  Part 1"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transcation_list = []     #transcation list is created in __init__ method & set to an empty list initially
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transcation_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            '''for above, create log of transcation and date, time of the local system.'''

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transcation(self):
        for date, amount in self.transcation_list:
            if amount > 0:
                tran_type = "Deposited"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print("{:6} {} on {} local time was {}".format(amount, tran_type, date, date.astimezone()))
            '''formattig is done accordingly and prints dat, time of local system using date.astimezone()'''

if __name__ == '__main__':
    dj = Account("DIVY", 0)
    dj.show_balance()

    dj.deposit(10000)
    dj.withdraw(2500)
    dj.withdraw(2000)
    dj.show_transcation()
