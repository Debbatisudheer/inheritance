class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.deposit(interest_amount)
        print(f"Interest of ${interest_amount} added. New balance: ${self.balance}")


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Transaction declined: Overdraft limit exceeded.")

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
        else:
            print("Transaction declined: Overdraft limit exceeded.")


class FixedDepositAccount(SavingsAccount):
    def __init__(self, account_number, balance, interest_rate, duration):
        super().__init__(account_number, balance, interest_rate)
        self.duration = duration

    def display_duration(self):
        print(f"Fixed Deposit Duration: {self.duration} months")


class PersonalLoan(SavingsAccount):
    def __init__(self, account_number, balance, loan_amount, interest_rate):
        super().__init__(account_number, balance, interest_rate)
        self.loan_amount = loan_amount

    def display_loan_amount(self):
        print(f"Loan Amount: ${self.loan_amount}")


class CarLoan(PersonalLoan):
    def __init__(self, account_number, balance, loan_amount, interest_rate):
        super().__init__(account_number, balance, loan_amount, interest_rate)

# Testing the bank management system with multilevel inheritance
if __name__ == "__main__":
    # Creating objects
    savings_acc = SavingsAccount("SA001", 1000, 0.05)
    checking_acc = CheckingAccount("CA001", 500, 100)
    fixed_deposit_acc = FixedDepositAccount("FDA001", 2000, 0.08, 12)
    car_loan = CarLoan("CL001", 0, 20000, 0.07)

    # Accessing superclass members
    savings_acc.display_balance()
    checking_acc.display_balance()
    fixed_deposit_acc.display_balance()
    car_loan.display_balance()

    # Reusability of code
    savings_acc.deposit(200)
    checking_acc.withdraw(600)
    fixed_deposit_acc.add_interest()
    car_loan.deposit(3000)

    # Display final balances and duration
    savings_acc.display_balance()
    checking_acc.display_balance()
    fixed_deposit_acc.display_balance()
    car_loan.display_balance()
