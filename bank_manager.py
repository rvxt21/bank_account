from bank_account import (
    BankAccount,
    InsufficientFundsError,
    NegativeAmountError,
)


class InvalidUserInputError(Exception):
    pass


class InvalidChoiceError(Exception):
    pass


class BankManager:
    def __init__(self, bank_account: BankAccount):
        self.is_running = True
        self.account = bank_account
        self.menu_options = {
            1: self._handle_deposit,
            2: self._handle_withdraw,
            3: self._handle_check_balance,
            4: self._exit,
        }

    def start(self):
        while self.is_running:
            try:
                help_string = self._get_user_input_hint()
                user_input = self._get_user_input(help_string)
                action = self._validate_action_key(user_input)
                action()
            except (
                InvalidUserInputError,
                InvalidChoiceError,
                NegativeAmountError,
                InsufficientFundsError,
            ) as e:
                print(f"Error: {e}")

    def _validate_action_key(self, user_input: int) -> any:
        try:
            action = self.menu_options[user_input]
            return action
        except KeyError:
            raise InvalidChoiceError(
                "Choice not found. Was looking for choice from menu"
            )

    def _get_user_input(self, help_string: str) -> int:
        user_input = input(help_string)
        user_int_input = self._convert_user_input_to_int(user_input)
        return user_int_input

    @staticmethod
    def _get_user_input_hint() -> str:
        return (
            "Please choose options (type the number):"
            " 1. Deposit, 2. Withdraw, 3. Check Balance, 4. Exit \n"
        )

    def _convert_user_input_to_int(self, user_input: str) -> int:
        try:
            user_int_input = int(user_input)
            return user_int_input
        except ValueError:
            raise InvalidUserInputError(
                "Value error: Expected a numeric digit, but received text."
            )

    def _exit(self):
        self.is_running = False

    @staticmethod
    def _get_user_input_deposit_hint() -> str:
        return "Enter the amount to add to the account. \n"

    def _handle_deposit(self):
        hint = self._get_user_input_deposit_hint()
        amount = self._get_user_input(hint)
        self.account.deposit(amount)

    @staticmethod
    def _get_user_input_withdraw_hint() -> str:
        return "Enter the amount to withdraw from your account. \n"

    def _handle_withdraw(self):
        hint = self._get_user_input_withdraw_hint()
        amount = self._get_user_input(hint)
        self.account.withdraw(amount)

    def _handle_check_balance(self):
        print(f"Current Balance: ${self.account.current_balance()}")
