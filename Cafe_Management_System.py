class MenuItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Order:
    def __init__(self, id, name, quantity, total, user_name, user_contact):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.total = total
        self.user_name = user_name
        self.user_contact = user_contact

def display_menu(menu):
    print("\nMenu:")
    for item in menu:
        print(f"{item.id}. {item.name} - ${item.price:.2f}")

def take_multiple_orders(menu, orders):
    try:
        user_name = input("Enter your name: ")
        
        # Validate the 10-digit mobile number
        while True:
            user_contact = input("Enter your 10-digit contact number: ")
            if len(user_contact) == 10 and user_contact.isdigit():
                break
            else:
                print("Invalid contact number. Please enter a 10-digit number.")

        print("\nEnter your orders one by one. Type 'done' after entering all orders.")

        while True:
            id_input = input("Enter item ID (or 'done' to finish): ")
            if id_input.lower() == 'done':
                break
            
            try:
                id = int(id_input)
                item = next((item for item in menu if item.id == id), None)
                if item:
                    quantity = int(input(f"Enter quantity for {item.name}: "))
                    total = item.price * quantity
                    orders.append(Order(id, item.name, quantity, total, user_name, user_contact))
                else:
                    print(f"Invalid item ID: {id}. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numeric values for item ID and quantity.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")

def display_orders(orders):
    if not orders:
        print("\nNo orders placed yet.")
        return
    print("\nOrders:")
    for order in orders:
        print(f"Order ID: {order.id}, Item: {order.name}, Quantity: {order.quantity}, Total: ${order.total:.2f}, User: {order.user_name}, Contact: {order.user_contact}")

def calculate_bill(orders):
    return sum(order.total for order in orders)

def save_orders(orders):
    with open("orders.txt", "w") as file:
        for order in orders:
            file.write(f"Order ID: {order.id}, Item: {order.name}, Quantity: {order.quantity}, Total: ${order.total:.2f}, User: {order.user_name}, Contact: {order.user_contact}\n")
    print("Orders saved to orders.txt")

def main():
    try:
        with open("menu.txt", "r") as file:
            menu = []
            for line in file:
                parts = line.strip().split()
                id = int(parts[0])
                price = float(parts[-1])
                name = ' '.join(parts[1:-1])
                menu.append(MenuItem(id, name, price))
    except FileNotFoundError:
        print("Error opening menu file.")
        return
    except ValueError:
        print("Error reading menu file content.")
        return

    orders = []

    while True:
        print("\nHeyy welcome To Our cafe")
        print("\n1. Display Menu\n2. Take Orders\n3. Display Orders\n4. Calculate Bill\n5. Save Orders\n6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_menu(menu)
            elif choice == 2:
                take_multiple_orders(menu, orders)
            elif choice == 3:
                display_orders(orders)
            elif choice == 4:
                print(f"Total Bill: ${calculate_bill(orders):.2f}")
            elif choice == 5:
                save_orders(orders)
            elif choice == 6:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")

if __name__ == "__main__":
    main()
