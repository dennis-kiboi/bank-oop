class BankAccount:
    bank_name = "PyBank"  # Class attribute/variable
    _accounts = {}
    _next_id = 1000  # shared counter

    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
        self.customer_id = None

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

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "balance": self.balance,
            "customer_id": self.customer_id
        }

    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id += 1
            account_id = f"ACC{cls._next_id}"

            if account_id not in cls._accounts:
                return account_id

    @classmethod
    def create(cls, balance=0):
        account_id = cls._generate_id()
        account = cls(account_id, balance)
        cls._accounts[account_id] = account
        return account

    @classmethod
    def get(cls, account_id):
        return cls._accounts.get(account_id)

    @classmethod
    def all(cls):
        return list(cls._accounts.values())

    @staticmethod
    def _validate_amount(amount, label):
        if amount <= 0:
            raise ValueError(f"{label} must be positive.")

    def __repr__(self):
        return f"BankAccount(account_id={self.account_id!r}, balance={self.balance!r})"