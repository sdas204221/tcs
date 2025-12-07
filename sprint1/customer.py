# customer.py

class Customer:
    def __init__(self,customer_id, name, email, password, address, contact):
        self.customer_id=customer_id
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.contact = contact

    def save(self):
        # Mock save, later can connect to DB
        print("\n[INFO] Customer details saved successfully!\n")
