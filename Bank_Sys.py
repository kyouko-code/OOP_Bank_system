class BankAccount:
    def __init__(self, balance, name, secret):
        self.__balance = balance
        self.name = name
        self.__secret = secret
    
    def withdraw(self, amount, secret):
        print(f"Withdrawing {amount} from {self.name}'s account.")
        if secret == self.__secret:

            remain = self.__balance - amount
            if remain < 0:
                print("Insufficient funds. Current balance")
            else:
                self.__balance = remain
                print("Withdrawal successful.")
                print(f"Remaining balance: {self.__balance}")
        else:
            print("invalid secret code. Please try again.")
    
    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name}'s balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def deposit(self, amount, secret):
        print(f"Depositing {amount} to {self.name}'s account.")
        if secret == self.__secret:
            self.__balance += amount
            print("Deposit successful.")
            print(f"New balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def payment(self, service_type, amount, secret):
        print(f"Processing payment for {service_type} from {self.name}'s account.")
        if secret == self.__secret:
            remain = self.__balance - amount
            if remain < 0:
                print("Insufficient funds. Payment failed.")
            else:
                self.__balance = remain
                print("Payment successful.")
                print(f"Remaining balance: {self.__balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def transfer(self, to_account, amount, secret):
        print(f"Transferring {amount} from {self.name} to {to_account.name}.")
        if secret == self.__secret:
            if self.__balance < amount:
                print("Insufficient funds. Transfer failed.")
            else:
                self.__balance -= amount
                to_account.__balance += amount
                print("Transfer successful.")
                print(f"{self.name}'s new balance: {self.__balance}")
                print(f"{to_account.name}'s new balance: {to_account.__balance}")
        else:
            print("Invalid secret code. Please try again.")


dara = BankAccount(balance=20000, name="dara", secret="1234")
visal = BankAccount(balance=5000, name="visal", secret="5678")

accounts = {"dara": dara, "visal": visal}

def display_menu():
    print("\n=== Bank Account Menu ===")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Payment")
    print("5. Transfer")
    print("6. Exit")
    print("========================\n")

while True:
    display_menu()
    choice = input("Select an option (1-6): ")
    
    if choice == "1":
        account_name = input("Enter account name : ").lower()
        if account_name in accounts:
            secret = input("Enter secret code: ")
            accounts[account_name].check_balance(secret)
        else:
            print("Invalid account name.")
    
    elif choice == "2":
        account_name = input("Enter account name : ").lower()
        if account_name in accounts:
            amount = float(input("Enter the amount to withdraw: "))
            secret = input("Enter secret code: ")
            accounts[account_name].withdraw(amount, secret)
        else:
            print("Invalid account name.")
    
    elif choice == "3":
        account_name = input("Enter account name : ").lower()
        if account_name in accounts:
            amount = float(input("Enter the amount to deposit: "))
            secret = input("Enter secret code: ")
            accounts[account_name].deposit(amount, secret)
        else:
            print("Invalid account name.")
    
    elif choice == "4":
        account_name = input("Enter account name : ").lower()
        if account_name in accounts:
            service_type = input("Enter service type: ")
            amount = float(input("Enter the amount to pay: "))
            secret = input("Enter secret code: ")
            accounts[account_name].payment(service_type, amount, secret)
        else:
            print("Invalid account name.")
    
    elif choice == "5":
        from_account = input("Enter sender account name : ").lower()
        to_account = input("Enter receiver account name : ").lower()
        if from_account in accounts and to_account in accounts:
            amount = float(input("Enter the amount to transfer: "))
            secret = input("Enter secret code: ")
            accounts[from_account].transfer(accounts[to_account], amount, secret)
        else:
            print("Invalid account name(s).")
    
    elif choice == "6":
        print("Exiting... Thank you for using our bank!")
        break
    
    else:
        print("Invalid option. Please try again.")

