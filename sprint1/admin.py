# admin.py
import json
import os
from mock_db import CUSTOMER_FILE, read_json

def get_customers_by_domain(domain):
    """
    Returns a list of customers whose email ends with the given domain
    """
    all_customers = read_json(CUSTOMER_FILE)
    # Filter only active customers
    matched = [c for c in all_customers if c["email"].split("@")[-1]==domain]
    return sorted(matched, key=lambda x: x["customer_id"])

def main():
    print("=== ADMIN: List Customers by Email Domain ===\n")
    domain_input = input("Enter Email Domain (e.g., gmail.com, yahoo.com): ").strip()
    if not domain_input:
        print("No domain entered. Exiting.")
        return

    matched_customers = get_customers_by_domain(domain_input)
    if matched_customers:
        print(f"\nCustomers with domain '{domain_input}':\n")
        for c in matched_customers:
            print(f"{c['customer_id']} {c['name']} {c['email']}")
    else:
        print(f"\nNo such customer is registered with {domain_input}")

if __name__ == "__main__":
    main()
