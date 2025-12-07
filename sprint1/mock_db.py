# mock_db.py
import json
import os

# File paths
CUSTOMER_FILE = "customers.json"
TRANSACTION_FILE = "transactions.json"
PRODUCT_FILE = "products.json"

# --- Helper functions ---
def read_json(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def write_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# --- Customer operations ---
def save_customer(customer):
    customers = read_json(CUSTOMER_FILE)
    # Check if customer_id exists, update
    for idx, c in enumerate(customers):
        if c["customer_id"] == customer.customer_id:
            customers[idx] = customer.__dict__
            write_json(CUSTOMER_FILE, customers)
            return
    # Else, add new
    customers.append(customer.__dict__)
    write_json(CUSTOMER_FILE, customers)

def get_all_customers():
    return read_json(CUSTOMER_FILE)

# --- Transaction operations ---
def save_transaction(transaction):
    transactions = read_json(TRANSACTION_FILE)
    transactions.append(transaction)
    write_json(TRANSACTION_FILE, transactions)

def get_all_transactions():
    return read_json(TRANSACTION_FILE)

# --- Products (optional) ---
def get_all_products():
    return read_json(PRODUCT_FILE)

def save_products(products):
    write_json(PRODUCT_FILE, products)

# mock_db.py
def login_customer(customer_id, password):
    customers = read_json(CUSTOMER_FILE)
    for c in customers:
        if c["customer_id"] == customer_id and c["password"] == password:
            from customer import Customer
            return Customer(**c)
    return None

