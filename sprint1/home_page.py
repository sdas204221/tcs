# home_page.py
from cart_page import cart_page
from profile_page import my_profile
from mock_db import get_all_products

def home_page(cart, customer):
    products = get_all_products()

    while True:
        print("\n========== HOME PAGE ==========\n")
        print("Available Products:")
        for p in products:
            print(f"{p['id']}. {p['name']} - ₹{p['price']}")

        print("\nOptions:")
        print(" A - Add product to cart")
        print(" C - View Cart")
        print(" P - My Profile")
        print(" E - Exit")

        choice = input("\nEnter option: ").upper()

        if choice == "A":
            try:
                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))
                found = False
                for p in products:
                    if p["id"] == pid:
                        cart.append({"product": p, "qty": qty})
                        print("Added to cart!")
                        found = True
                        break
                if not found:
                    print("Invalid Product ID!")
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "C":
            cart_page(cart, customer)

        elif choice == "P":
            my_profile(customer)

        elif choice == "E":
            exit()
        else:
            print("Invalid Option!")
