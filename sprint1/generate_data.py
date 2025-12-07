import json
import random

# --- Configuration ---
NUM_ENTRIES_TO_ADD_P = 2
NUM_ENTRIES_TO_ADD_C = 10

# --- Product Data Generation ---

def generate_random_product():
    """Generates a dictionary for a single random product entry."""
    # List of common grocery items with rough units/sizes
    items = [
        ("Banana (1 kg)", 65), ("Tomato (500g)", 30), ("Potatoes (2 kg)", 80),
        ("Rice (5 kg bag)", 450), ("Lentils (1 kg)", 110), ("Chicken Breast (500g)", 220),
        ("Eggs (1 dozen)", 70), ("Cooking Oil (1 L)", 180), ("Sugar (1 kg)", 45),
        ("Coffee Powder (250g)", 300), ("Tea Bags (100 ct)", 150), ("Yogurt (500g)", 95),
        ("Cheese Block (200g)", 140), ("Orange Juice (1 L)", 130), ("Cookies (300g)", 60)
    ]

    name, base_price = random.choice(items)

    # Randomizing price slightly around the base price
    price = base_price + random.randint(-15, 15)
    price = max(10, price)  # Ensure price is at least 10

    # Randomizing available quantity
    available_qty = random.choices([0, 1, 5, random.randint(10, 200)], weights=[5, 5, 20, 70], k=1)[0]

    return {
        "name": name,
        "price": price,
        "available_qty": available_qty
    }

def generate_products_data(starting_id, num_entries):
    """Generates a list of random product dictionaries."""
    products = []
    for i in range(num_entries):
        product = generate_random_product()
        product["id"] = starting_id + i
        products.append(product)
    return products

# --- Customer Data Generation ---

def generate_random_customer():
    """Generates a dictionary for a single random customer entry."""
    first_names = ["Raj", "Priya", "Amit", "Sneha", "Vikram", "Neha", "Arjun", "Kavita", "Sandeep", "Deepa"]
    last_names = ["Sharma", "Verma", "Singh", "Reddy", "Patel", "Joshi", "Das", "Chopra", "Malhotra", "Goyal"]
    email_domains = ["gmail.com", "outlook.com", "yahoo.in", "mymail.co", "workcorp.com", "consulting.net"]
    statuses = ["Active", "Inactive"]
    streets = ["Main St", "Cross Rd", "Park View", "MG Road", "Temple St"]
    cities = ["Kolkata", "Mumbai", "Delhi", "Bangalore", "Chennai"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"

    # Creating email with variety in format and domains
    email_prefix = "".join(random.choices([first_name.lower(), last_name.lower(), str(random.randint(10, 999))], k=random.randint(2, 3)))
    email = f"{email_prefix}@{random.choice(email_domains)}"

    # Randomizing contact number and password
    contact = str(random.randint(6000000000, 9999999999))
    password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))

    # Randomizing address
    address = f"{random.choice(['Flat', 'House'])} {random.randint(10, 99)}, {random.choice(streets)}, {random.choice(cities)}"

    return {
        "name": full_name,
        "email": email,
        "password": password,
        "address": address,
        "contact": contact,
        "status": random.choice(statuses)
    }

def generate_customers_data(starting_id, num_entries):
    """Generates a list of random customer dictionaries."""
    customers = []
    for i in range(num_entries):
        customer = generate_random_customer()
        customer["customer_id"] = starting_id + i
        customers.append(customer)
    return customers

# --- Main Script Execution ---

def load_and_append_data(filename, data_generator_func, id_field, num_entries):
    """Loads existing JSON data, generates new entries, and saves the combined data."""
    try:
        with open(filename, 'r') as f:
            existing_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Start with an empty list if file doesn't exist or is empty/corrupt
        existing_data = []

    # Determine the starting ID for new entries
    if existing_data:
        # Find the maximum existing ID and start the new IDs from the next number
        max_id = max(item.get(id_field, 0) for item in existing_data)
        starting_id = max_id + 1
    else:
        starting_id = 1

    # Generate new random data
    new_data = data_generator_func(starting_id, num_entries)

    # Combine and save
    combined_data = existing_data + new_data
    with open(filename, 'w') as f:
        json.dump(combined_data, f, indent=4)

    print(f"✅ Successfully added {num_entries} new entries to {filename}.")
    print(f"Total entries in {filename}: {len(combined_data)}")


if __name__ == "__main__":
    print(f"--- Adding {NUM_ENTRIES_TO_ADD_P} Product and {NUM_ENTRIES_TO_ADD_C} Customer Random Entries ---")

    # 1. Update products.json
    load_and_append_data(
        filename="products.json",
        data_generator_func=generate_products_data,
        id_field="id",
        num_entries=NUM_ENTRIES_TO_ADD_P
    )

    # 2. Update customers.json
    load_and_append_data(
        filename="customers.json",
        data_generator_func=generate_customers_data,
        id_field="customer_id",
        num_entries=NUM_ENTRIES_TO_ADD_C
    )