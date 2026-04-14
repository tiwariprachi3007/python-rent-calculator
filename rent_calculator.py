def calculate_share(rent, food, units, charge, persons):
    """Calculate per-person rent share."""
    total_bill = rent + food + (units * charge)
    return total_bill / persons


def get_int_input(prompt):
    """Safely get integer input from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Rent Calculator ===")
    rent = get_int_input("Enter your hostel/flat rent: ")
    food = get_int_input("Enter the amount of food ordered: ")
    units = get_int_input("Enter the electricity units consumed: ")
    charge = get_int_input("Enter the charge per unit: ")
    persons = get_int_input("Enter the number of persons living: ")

    if persons <= 0:
        print("Number of persons must be greater than 0.")
        return

    share = calculate_share(rent, food, units, charge, persons)
    print(f"\nEach person will pay = {share:.2f}")


if __name__ == "__main__":
    main()
