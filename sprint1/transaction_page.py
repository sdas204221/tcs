# transaction_page.py
import random

from generate_invoice import generate_invoice

def transaction_page(cart, customer):
    if len(cart) == 0:
        print("\n[ERROR] Cart empty! Cannot checkout.")
        return

    # Default values
    discount = 0
    extra_charges = 25   # example delivery charge
    gst_rate = 0.05       # 5% GST

    while True:
        print("\n========== TRANSACTION PAGE ==========\n")

        # --- Calculate prices ---
        total_product_price = sum(item["product"]["price"] * item["qty"] for item in cart)
        gst_amount = total_product_price * gst_rate
        order_total = total_product_price - discount + extra_charges + gst_amount

        # --- Payment Method ---
        print("Choose Payment Method:")
        print(" 1 - Cash On Delivery (COD)")
        print(" 2 - UPI")
        print(" 3 - Credit Card")
        print(" 4 - Debit Card")
        print(" 5 - Net Banking")
        payment_choice = input("\nEnter option (1-5): ")

        if payment_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid option! Try again.")
            continue

        # --- Price Summary ---
        print("\n------ PRICE SUMMARY ------")
        print(f"Total Product Price : ₹{total_product_price}")
        print(f"Total Discount      : ₹{discount}")
        print(f"Extra Charges       : ₹{extra_charges}")
        print(f"GST (5%)            : ₹{gst_amount:.2f}")
        print("---------------------------")
        print(f"Order Total         : ₹{order_total:.2f}")
        print("---------------------------\n")

        print("Options:")
        print(" D - Edit Discount")
        print(" E - Edit Extra Charges")
        print(" P - Proceed to Buy")
        print(" B - Back to Cart")

        choice = input("\nEnter choice: ").upper()

        # --- Update Discount ---
        if choice == "D":
            try:
                discount = float(input("Enter new discount amount: "))
            except:
                print("Invalid input!")

        # --- Update Charges ---
        elif choice == "E":
            try:
                extra_charges = float(input("Enter new extra charges: "))
            except:
                print("Invalid input!")

        # --- Proceed to Buy ---
        elif choice == "P":
            generate_invoice(cart, customer, order_total)
            cart.clear()  # empty cart after successful transaction
            return  # go back to home

        elif choice == "B":
            return

        else:
            print("Invalid choice! Try again.")
