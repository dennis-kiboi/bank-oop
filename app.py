from bank_account import BankAccount
from customer import Customer

# Create Customer instances
amina = Customer.create("Amina Otieno")
brian = Customer.create("Brian Mwangi")

print(amina.customer_id)
print(Customer.get("CUS1001"))
