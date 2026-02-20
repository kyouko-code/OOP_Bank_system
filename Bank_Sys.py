class BankAccount:
    def __init__(self, balance, name, secret):
        self._balance = balance
        self.name = name
        self.__secret = secret
    
    def _verify_secret(self, secret):
        return self.__secret == secret
    
    def withdraw(self, amount, secret):
        print(f"Withdrawing {amount} from {self.name}'s account.")
        if secret == self.__secret:

            remain = self._balance - amount
            if remain < 0:
                print("Insufficient funds. Current balance")
            else:
                self._balance = remain
                print("Withdrawal successful.")
                print(f"Remaining balance: {self._balance}")
        else:
            print("invalid secret code. Please try again.")
    
    def check_balance(self, secret):
        if secret == self.__secret:
            print(f"{self.name}'s balance: {self._balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def deposit(self, amount, secret):
        print(f"Depositing {amount} to {self.name}'s account.")
        if secret == self.__secret:
            self._balance += amount
            print("Deposit successful.")
            print(f"New balance: {self._balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def payment(self, service_type, amount, secret):
        print(f"Processing payment for {service_type} from {self.name}'s account.")
        if secret == self.__secret:
            remain = self._balance - amount
            if remain < 0:
                print("Insufficient funds. Payment failed.")
            else:
                self._balance = remain
                print("Payment successful.")
                print(f"Remaining balance: {self._balance}")
        else:
            print("Invalid secret code. Please try again.")
    
    def transfer(self, to_account, amount, secret):
        print(f"Transferring {amount} from {self.name} to {to_account.name}.")
        if secret == self.__secret:
            if self._balance < amount:
                print("Insufficient funds. Transfer failed.")
            else:
                self._balance -= amount
                to_account._balance += amount
                print("Transfer successful.")
                print(f"{self.name}'s new balance: {self._balance}")
                print(f"{to_account.name}'s new balance: {to_account._balance}")
        else:
            print("Invalid secret code. Please try again.")

class SavingsAccount(BankAccount):
    
    def check_balance(self, secret):
        if self._verify_secret(secret):
            print(f'Your old balance is ${self._balance}')
            self._balance += 10
            print(f'Your savings account has ${self._balance}')
        else:
            print("\nIncorrect secret!")
    
    def calculate_interest(self):
        interest_rate = 0.05
        interest = self._balance * interest_rate
        print(f"Interest for {self.name}'s savings account: {interest}")

class StudentBankAccount(BankAccount):
    
    def withdraw(self, amount, secret):
        if amount > 500:
            print("Maximum withdrawal amount is $500!")
        elif self._BankAccount__secret == secret:
            remain = self._balance - amount
            if remain < 0:
                print("Balance isn't enough to withdraw!")
            else:
                self._balance = remain
                print('-' * 23)
                print('| Withdraw successfully |')
                print('-' * 23)
                print(f'Your remaining balance is  ${self._balance}')
        else:
            print("Invalid secret code. Please try again.")

class PremiumSaving(SavingsAccount):
    
    def deposit(self, amount, secret):
        if self._verify_secret(secret):
            interest = amount * 0.02
            remain = self._balance + amount + interest
            self._balance = remain
            print('-' * 22)
            print('| deposit successfully |')
            print('-' * 22)
            print(f'Your premium saving account has ${self._balance} with interest 2% ${interest}  of amount')
        else:
            print("Invalid secret code. Please try again.")

class BusinessAccount(BankAccount):
    
    def take_loan(self):
        amount = float(input("Enter the loan amount: $"))
        interest_rate = 0.7
        total_payment = amount + (amount * interest_rate / 100)
        print("Borrower Name:", self.name)
        print("Loan Amount:", amount)
        print(f'Interest Rate: {interest_rate}%')
        print("Total Payment:", total_payment)
        
        choice = input("Do you borrow money? (yes/no): ")
        if choice == 'yes':
            self._balance += amount
            print(f'\nYour Business Account has ${self._balance}')
        elif choice == 'no':
            return

dara = BankAccount(balance=20000, name="dara", secret="1234")
viva = SavingsAccount(balance=3000, name="viva", secret="8765")
vanak = StudentBankAccount(balance=1500, name="vanak", secret="4321")
jusit = PremiumSaving(balance=5000, name="jusit", secret="9876")
kiki = BusinessAccount(balance=12000, name="kiki", secret="0987")

accounts = {"dara": dara, "viva": viva, "vanak": vanak, "jusit": jusit, "kiki": kiki}

while True:
    print("\n=== Bank Account Menu ===")
    print("1. Bank Account")
    print("2. Savings Account")
    print("3. Student Bank Account")
    print("4. Premium Saving Account")
    print("5. Business Account")
    print("6. Exit")
    print("========================\n")
    
    account_type = input("Select account type (1-6): ")
    
    if account_type == "6":
        print("Exiting... Thank you for using our bank!")
        break
    
    if account_type not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please try again.")
        continue
    
    account_name = input("Enter your account name: ").lower()
    if account_name not in accounts:
        print("Invalid account name.")
        continue
    
    secret = input("Enter your secret code: ")
    if not accounts[account_name]._verify_secret(secret):
        print("Incorrect secret!")
        continue
    
    acc_login = accounts[account_name]
    print(f"\nWelcome {acc_login.name}!")
    
    while True:
        print("\n=== Menu ===")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Payment")
        print("5. Transfer")
        print("6. Calculate Interest")
        
        if isinstance(acc_login, BusinessAccount):
            print("7. Take Loan")
            print("8. Logout")
            choice = input("Select an option (1-8): ")
        else:
            print("7. Logout")
            choice = input("Select an option (1-7): ")
        
        if choice == "1":
            acc_login.check_balance(secret)
        
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            acc_login.withdraw(amount, secret)
        
        elif choice == "3":
            amount = float(input("Enter the amount to deposit: "))
            acc_login.deposit(amount, secret)
        
        elif choice == "4":
            print("\n=== Payment Type ===")
            print("1. Electricity Bill")
            print("2. Water Bill")
            print("3. Internet Bill")
            print("4. Phone Bill")
            print("5. Other")
            payment_choice = input("Select payment type (1-5): ")
            
            payment_types = {
                "1": "Electricity Bill",
                "2": "Water Bill",
                "3": "Internet Bill",
                "4": "Phone Bill",
                "5": "Other"
            }
            
            if payment_choice in payment_types:
                amount = float(input("Enter the amount to pay: "))
                acc_login.payment(payment_types[payment_choice], amount, secret)
            else:
                print("Invalid payment type.")
        
        elif choice == "5":
            to_name = input("Enter receiver account name: ").lower()
            if to_name in accounts:
                amount = float(input("Enter the amount to transfer: "))
                acc_login.transfer(accounts[to_name], amount, secret)
            else:
                print("Invalid account name.")
        
        elif choice == "6":
            if isinstance(acc_login, SavingsAccount):
                acc_login.calculate_interest()
            else:
                print("Interest calculation is only available for Savings/Premium Saving accounts.")
        
        elif choice == "7" and isinstance(acc_login, BusinessAccount):
            acc_login.take_loan()
        
        elif (choice == "7" and not isinstance(acc_login, BusinessAccount)) or (choice == "8" and isinstance(acc_login, BusinessAccount)):
            print("Logging out...")
            break
        
        else:
            print("Invalid option. Please try again.")

