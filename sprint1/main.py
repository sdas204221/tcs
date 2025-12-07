# main.py
import random
from customer import Customer
from profile_page import my_profile
from home_page import home_page

# main.py
import random
from customer import Customer
from home_page import home_page
from mock_db import login_customer, get_all_customers, save_customer

def register():
    print("\n========== REGISTER ==========\n")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    address = input("Address: ").strip()
    contact = input("Contact No: ").strip()
    customer_id = random.randint(1000,9999)
    customer = Customer(customer_id, name, email, password, address, contact)
    customer.save()
    print(f"Registered Successfully! Your Customer ID: {customer.customer_id}")
    return customer

def login():
    print("\n========== LOGIN ==========\n")
    try:
        customer_id = int(input("Customer ID: "))
        password = input("Password: ").strip()
        customer = login_customer(customer_id, password)
        if customer:
            print(f"Login Successful! Welcome {customer.name}")
            return customer
        else:
            print("Invalid Customer ID or Password.")
            return None
    except ValueError:
        print("Customer ID must be a number.")
        return None

def start_app():
    cart = []

    while True:
        print("\n1 - Login\n2 - Register\n3 - Exit")
        choice = input("Choose option: ").strip()
        if choice == "1":
            customer = login()
            if customer:
                if customer.status == "Active":
                    home_page(cart, customer)
                else:
                    # Inactive profile menu
                    my_profile(customer)
        elif choice == "2":
            customer = register()
            if customer:
                home_page(cart, customer)
        elif choice == "3":
            exit()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    start_app()
