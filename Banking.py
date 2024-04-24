class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Current balance for {self.name}: ${self.balance}")


def main():
    print("Welcome to the Simple Banking System!")
    print("Please create your account.")
    name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: $"))
    account = Account(name, initial_balance)

    while True:
        print("\nChoose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the Simple Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
