import os
from mock_db import PRODUCT_FILE, get_all_products, save_products


def initialize_products():
    """Create default products if file is empty"""
    if not os.path.exists(PRODUCT_FILE) or len(get_all_products()) == 0:
        products = [
            {"id": 1, "name": "Apple (1 kg)", "price": 120},
            {"id": 2, "name": "Milk (1 L)", "price": 45},
            {"id": 3, "name": "Bread", "price": 28},
        ]
        save_products(products)
if __name__ == "__main__":
    initialize_products()
