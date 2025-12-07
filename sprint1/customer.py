# customer.py

class Customer:
    def __init__(self, name, email, password, address, contact):
        self.name = name
        self.email = email
        self.password = password
        self.address = address
        self.contact = contact

    def save(self):
        # Mock save, later can connect to DB
        print("\n[INFO] Customer details saved successfully!\n")
