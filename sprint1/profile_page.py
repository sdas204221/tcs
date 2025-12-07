# profile_page.py

def my_profile(customer):
    while True:
        print("\n========== MY PROFILE ==========\n")
        print(f"Customer Name : {customer.name}")
        print(f"Customer ID    : {customer.customer_id}")
        print(f"Email         : {customer.email}")
        # print(f"Password      : {customer.password}")
        print(f"Address       : {customer.address}")
        print(f"Contact No    : {customer.contact}")
        print("\nOptions:")
        print(" 1 - Update Details")
        print(" 2 - Save")
        print(" 3 - Go to Home Page")
        print(" 4 - Back")

        choice = input("\nEnter option: ")

        if choice == "1":
            customer.name = input("New Name: ") or customer.name
            customer.email = input("New Email: ") or customer.email
            customer.password = input("New Password: ") or customer.password
            customer.address = input("New Address: ") or customer.address
            customer.contact = input("New Contact: ") or customer.contact
            print("\n[INFO] Update Done. Don't forget to Save.")

        elif choice == "2":
            customer.save()

        elif choice == "3":
            return  # routing back to home

        elif choice == "4":
            return()

        else:
            print("Invalid choice!")
