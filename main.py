from bank_account import BankAccount
from bank_manager import BankManager

if __name__ == "__main__":
    bank_account = BankAccount("Anastasiia K.", 0)
    bank_manager = BankManager(bank_account)
    bank_manager.start()
