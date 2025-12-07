# customer.py
from mock_db import save_customer

class Customer:
    def __init__(self, customer_id, name, email, password, address, contact, status="Active"):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.contact = contact
        self.status = status  # Active or Inactive

    def save(self):
        save_customer(self)
        print(f"\n[INFO] Customer {self.customer_id} saved to mock DB!")

    def unregister(self):
        self.status = "Inactive"
        self.save()
        print("\nYour Profile is Inactived Successfully")
        from main import start_app
        start_app()

    def activate(self):
        self.status = "Active"
        self.save()
        print("\nYour Profile is Activated Successfully")
