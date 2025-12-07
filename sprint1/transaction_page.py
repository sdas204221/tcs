# transaction_page.py
def transaction_page(cart):
    print("\n========== TRANSACTION PAGE ==========\n")

    if len(cart) == 0:
        print("Cart is empty. Cannot checkout.")
        return

    total = 0
    print("Invoice:")
    for item in cart:
        p = item["product"]
        qty = item["qty"]
        price = p["price"] * qty
        total += price
        print(f"{p['name']} x{qty} = ₹{price}")

    print("\nTotal Amount Payable =", total)
    input("\nPress Enter to confirm payment...")

    print("\nPayment Successful! Transaction completed.")
    cart.clear()  # empty cart after payment
    input("\nPress Enter to return to Home...")
