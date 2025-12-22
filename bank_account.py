class NegativeAmountError(Exception):
    pass


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(
        self, account_holder: str = "Default holder", balance: int = 0
    ):
        self.account_holder: str = account_holder
        self.balance: int = balance

    def deposit(self, amount: int):
        try:
            self.validate_negative_amount(amount)
            self.balance += amount
        except NegativeAmountError:
            print("Not possible to process negative amount")

    def withdraw(self, amount: int):
        try:
            self.validate_negative_amount(amount)
            self.validate_sufficient_balance(amount)
            self.balance -= amount
        except (NegativeAmountError, InsufficientFundsError) as e:
            print(f"Error transaction: {e}")

    def current_balance(self):
        return self.balance

    def validate_negative_amount(self, amount: int):
        if amount < 0:
            raise NegativeAmountError("Amount must be positive")

    def validate_sufficient_balance(self, amount: int):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money")


my_bank_account = BankAccount("Anastasiia", 100)
print(my_bank_account.current_balance())
my_bank_account.deposit(1000)
print(my_bank_account.current_balance())
my_bank_account.withdraw(50)
print(my_bank_account.current_balance())
my_bank_account.withdraw(-50)
print(my_bank_account.current_balance())
