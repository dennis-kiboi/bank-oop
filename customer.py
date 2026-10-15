class Customer:
    _customers = {}
    _next_id = 1000

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.account_ids = []

    @classmethod
    def create(cls, name):
        customer_id = cls._generate_id()
        customer = cls(customer_id, name)
        cls._customers[customer_id] = customer
        return customer

    @classmethod
    def _generate_id(cls):
        while True:
            cls._next_id += 1
            customer_id = f"CUS{cls._next_id}"

            if customer_id not in cls._customers:
                return customer_id

    @classmethod
    def get(cls, customer_id):
        return cls._customers.get(customer_id)

    @classmethod
    def all(cls):
        return list(cls._customers.values())

    def __repr__(self):
        return f"Customer('{self.customer_id}', '{self.name}')"