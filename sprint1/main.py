# main.py
from customer import Customer
from profile_page import my_profile
from home_page import home_page

def start_app():
    cart = []

    # Mock registered user
    customer = Customer(
        name="Subhra",
        email="subhra@example.com",
        password="12345",
        address="Kolkata",
        contact="9876543210"
    )

    while True:
        # my_profile(customer)
        home_page(cart,customer)

if __name__ == "__main__":
    start_app()
