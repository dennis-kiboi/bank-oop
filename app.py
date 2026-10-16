import json

from bank_account import BankAccount
from customer import Customer

# Create Customer instances
amina = Customer.create("Amina Otieno")
brian = Customer.create("Brian Mwangi")

savings = BankAccount.create(5000)
current = BankAccount.create()

amina.add_account(savings)
amina.add_account(current)

# aminas_account_ids = amina.account_ids
# aminas_account_objects = [BankAccount.get(account_id) for account_id in aminas_account_ids]

# print(aminas_account_ids)
# print(aminas_account_objects)

def save_data(filename="bank_data.json"):
    data = {
        "customers": {
            customer_id: customer.to_dict() for customer_id, customer in Customer._customers.items()
        },
        "accounts": {
            account_id: account.to_dict() for account_id, account in BankAccount._accounts.items()
        }
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

save_data()