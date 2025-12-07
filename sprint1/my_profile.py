class Customer:
    def __init__(self, name, email, password, address, contact): 
        self.name = name[:50]         
        self.email = email
        self.password = password[:30] 
        self.address = address[:100]  
        self.contact = contact[:10]   

    def display_profile(self):    
        print("\n" + "="*40)
        print(f"   My Profile — {self.name}")
        print("="*40)
        print(f"1) Name         : {self.name}")
        print(f"2) Email        : {self.email}")
        print(f"3) Password     : {'*' * len(self.password)}")  
        print(f"4) Address      : {self.address}")
        print(f"5) Contact No.  : {self.contact}")
        print("="*40)

    def update_field(self, field_no, new_value):  
        if field_no == 1:
            self.name = new_value[:50]
        elif field_no == 2:
            self.email = new_value
        elif field_no == 3:
            self.password = new_value[:30]
        elif field_no == 4:
            self.address = new_value[:100]
        elif field_no == 5:    
            cleaned = ''.join(ch for ch in new_value if ch.isdigit())
            self.contact = cleaned[:10]
        else:
            print("Unknown field number.")

    def save(self):
        
        print("\nSaving profile...")
        
        if not self.name:
            print("Error: Name cannot be empty. Save failed.")
            return False
        if len(self.contact) != 10:
            print("Warning: Contact number is not 10 digits. Still saving (mock).")
        
        print("Profile saved (mock). Current values:")
        self.display_profile()
        return True


def get_registration_mock():
    return {
        "name": "Subhra Das",                       
        "email": "subhra@example.com",
        "password": "mysecretpassword",
        "address": "123, College Street, Kolkata",
        "contact": "9123456780"
    }


def my_profile(customer):
    while True:
        customer.display_profile()
        print("Options:")
        print(" U - Update a field")
        print(" S - Save (mock)")
        print(" E - Exit")
        choice = input("Choose an option (U/S/E): ").strip().upper()
        if choice == "U":
            try:
                field_no = int(input("Enter field number to update (1-5): ").strip())
                if field_no < 1 or field_no > 5:
                    print("Please choose a number between 1 and 5.")
                    continue
                new_val = input("Enter new value: ").strip()
                customer.update_field(field_no, new_val)
                print("Field updated. (Not yet saved until you choose Save.)")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "S":
            customer.mock_save()
            input("Press Enter to continue...")
        elif choice == "E":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please choose U, S, or E.")


if __name__ == "__main__":
    reg = get_registration_mock()
    customer = Customer(reg["name"], reg["email"], reg["password"], reg["address"], reg["contact"])
    my_profile(customer)
