from decimal import Decimal

class Checkbook:
    def __init__(self):
        self.balance = Decimal('0.00')

    def deposit(self, amount):
        try:
            amount = Decimal(amount)
            if amount < Decimal('0.00'):
                print("Invalid amount. Please enter a positive value.")
            else:
                self.balance += amount
                print("Deposited ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid numeric value.")

    def withdraw(self, amount):
        try:
            amount = Decimal(amount)
            if amount < Decimal('0.00'):
                print("Invalid amount. Please enter a positive value.")
            elif amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid amount. Please enter a valid numeric value.")

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = input("Enter the amount to deposit: $")
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = input("Enter the amount to withdraw: $")
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a valid numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()