# customer.py
from mock_db import save_customer

class Customer:
    def __init__(self, customer_id, name, email, password, address, contact):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.contact = contact

    def save(self):
        # Save to mock JSON DB
        save_customer(self)
        print("\n[INFO] Customer saved to mock DB!")
