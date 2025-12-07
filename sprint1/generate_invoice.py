import random


def generate_invoice(cart, customer, total_amount):
    print("\n========== INVOICE ==========\n")

    transaction_id = random.randint(100000, 999999)
    customer_id = random.randint(1000, 9999)  # mock customer ID
    product_ids = [item["product"]["id"] for item in cart]
    total_items = sum(item["qty"] for item in cart)

    print(f"Transaction ID : {transaction_id}")
    print(f"Customer ID    : {customer_id}")
    print(f"Product IDs    : {product_ids}")
    print(f"No of Items    : {total_items}")
    print(f"Total Amount   : ₹{total_amount:.2f}")

    print("\n[INFO] Transaction Saved to Transaction Table (Mock)")
    print("[INFO] Payment Successful! Order placed.\n")

    input("Press Enter to return to Home...")
