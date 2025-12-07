# home_page.py
from cart_page import cart_page
from profile_page import my_profile

PRODUCTS = [
    {"id": 1, "name": "Apple (1 kg)", "price": 120},
    {"id": 2, "name": "Milk (1 L)", "price": 45},
    {"id": 3, "name": "Bread", "price": 28},
]

def home_page(cart,customer):
    while True:
        print("\n========== HOME PAGE ==========\n")
        print("Available Products:")
        for p in PRODUCTS:
            print(f"{p['id']}. {p['name']} - ₹{p['price']}")

        print("\nOptions:")
        print(" A - Add product to cart")
        print(" C - View Cart")
        print(" P - My Profile")
        print(" E - Exit")

        choice = input("\nEnter option: ").upper()

        if choice == "A":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))

            for p in PRODUCTS:
                if p["id"] == pid:
                    cart.append({"product": p, "qty": qty})
                    print("Added to cart!")
                    break

        elif choice == "C":
            cart_page(cart)

        elif choice == "P":
            my_profile(customer)

        elif choice == "E":
            exit()
        else:
            print("Invalid Option!")
