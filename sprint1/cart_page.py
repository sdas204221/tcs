# cart_page.py
from transaction_page import transaction_page

def cart_page(cart,customer):
    while True:
        print("\n========== CART PAGE ==========\n")

        if len(cart) == 0:
            print("Your cart is empty.\n")
            print("1 - View Products")
            print("2 - Back to Home")
            ch = input("Enter choice: ")

            if ch == "1":
                return  # back to home
            elif ch == "2":
                return
            else:
                print("Invalid!")
        else:
            total = 0
            for i, item in enumerate(cart):
                p = item["product"]
                qty = item["qty"]
                line = p["price"] * qty
                total += line
                print(f"{i+1}. {p['name']} x{qty} = ₹{line}")

            print("\nTotal Amount =", total)
            print("\nOptions:")
            print(" D - Delete item")
            print(" O - Checkout")
            print(" B - Back to Home")

            choice = input("\nEnter option: ").upper()

            if choice == "D":
                idx = int(input("Enter item number: ")) - 1
                if 0 <= idx < len(cart):
                    cart.pop(idx)
                    print("Item removed!")
                else:
                    print("Invalid index!")

            elif choice == "O":
                transaction_page(cart,customer)

            elif choice == "B":
                return
