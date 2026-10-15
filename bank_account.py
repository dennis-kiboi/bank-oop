class BankAccount:
    bank_name = "PyBank"  # Class attribute/variable
    _accounts = {}
    _next_id = 1000  # shared counter

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Getter method
    @property
    def balance(self):
        return self._balance

    # Setter method
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:  # guard clauses
            raise ValueError("Balance cannot be negative")

        self._balance = new_balance

    def deposit(self, amount):
        # Deposit must be positive
        self._validate_amount(amount, "Deposit")
        self._balance += amount

    def withdraw(self, amount):
        self._validate_amount(amount, "Withdrawal")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    @classmethod
    def _generate_id(cls):
        cls._next_id += 1
        return f"ACC{cls._next_id}"

    @staticmethod
    def _validate_amount(amount, label):
        if amount <= 0:
            raise ValueError(f"{label} must be positive.")