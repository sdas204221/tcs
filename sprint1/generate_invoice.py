# generate_invoice.py
def generate_invoice(transaction):
    print("\n========== INVOICE ==========\n")

    print(f"Transaction ID : {transaction['transaction_id']}")
    print(f"Customer ID    : {transaction['customer_id']}")
    print(f"Products       :")
    for item in transaction["products"]:
        print(f"  {item['name']} x{item['qty']} = ₹{item['price']*item['qty']}")

    print(f"\nTotal Product Price : ₹{transaction['total_product_price']}")
    print(f"Discount            : ₹{transaction['discount']}")
    print(f"Extra Charges       : ₹{transaction['extra_charges']}")
    print(f"GST                 : ₹{transaction['gst']:.2f}")
    print(f"Order Total         : ₹{transaction['order_total']:.2f}")
    print(f"Total Items         : {transaction['total_items']}")

    print("\n[INFO] Transaction saved to mock DB. Payment successful!")
    input("Press Enter to return to Home...")
