def display_menu(menu):
    """Display the menu with item numbers, names, and prices."""
    print("\n--- Menu ---")
    for item_no, (item_name, item_price) in enumerate(menu.items(), start=1):
        print(f"{item_no}. {item_name} - ${item_price:.2f}")

def get_order(menu):
    """Prompt the user to select an item by number and return the item name and price."""
    while True:
        try:
            choice = int(input("\nEnter the number of the item you want to order: "))
            if 1 <= choice <= len(menu):
                item_name = list(menu.keys())[choice - 1]
                item_price = menu[item_name]
                return item_name, item_price
            else:
                print("Invalid choice. Please select a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def process_payment(total_cost):
    """Handle payment and return the change."""
    while True:
        try:
            cash = float(input(f"\nThe total cost is ${total_cost:.2f}. Enter cash amount: "))
            if cash >= total_cost:
                return cash - total_cost
            else:
                print("Insufficient amount. Please provide more cash.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def main():
    # Define the menu as a dictionary with item names and prices
    menu = {
        "Potato Marble": 5.99,
        "Fish and Chips": 8.99,
        "Spaghetti": 7.49,
        "Coleslaw": 4.99,
        "Sparkling Water": 1.99
    }

    # Display the menu
    display_menu(menu)

    # Get the user's order
    item_name, item_price = get_order(menu)
    print(f"\nYou selected: {item_name} - ${item_price:.2f}")

    # Process payment
    change = process_payment(item_price)

    # Display the result
    print(f"\nPayment successful! Your change is ${change:.2f}.")
    print("Thank you for your order!")

if __name__ == "__main__":
    main()