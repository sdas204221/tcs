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

                # Find the product by id
                product = next((p for p in products if p["id"] == pid), None)
                if not product:
                    print("Invalid Product ID!")
                    continue

                # Check if product already in cart by id
                cart_item = next((item for item in cart if item["id"] == pid), None)
                if cart_item:
                    cart_item["qty"] += qty
                    print(f"Updated quantity of {product['name']} in cart to {cart_item['qty']}")
                else:
                    # Add to cart with hidden id tracking
                    cart.append({
                        "id": pid,           # internal use only
                        "product": product,  # UI shows only name, price
                        "qty": qty
                    })
                    print("Added to cart!")

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
