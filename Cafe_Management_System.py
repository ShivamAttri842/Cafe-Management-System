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
        user_contact = input("Enter your contact number: ")
        print("\nEnter your orders in the format 'item_number quantity'. Type 'done' when finished.")
        
        while True:
            order_input = input("Enter item and quantity: ")
            if order_input.lower() == 'done':
                break
            
            parts = order_input.split()
            if len(parts) != 2:
                print("Invalid input. Please enter in the format 'item_number quantity'.")
                continue
            
            id = int(parts[0])
            quantity = int(parts[1])
            item = next((item for item in menu if item.id == id), None)
            
            if item:
                total = item.price * quantity
                orders.append(Order(id, item.name, quantity, total, user_name, user_contact))
            else:
                print(f"Invalid item number: {id}. Please try again.")
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
        print("\n1. Display Menu\n2. Take Order\n3. Take Multiple Orders\n4. Display Orders\n5. Calculate Bill\n6. Save Orders\n7. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_menu(menu)
            elif choice == 2:
                take_multiple_orders(menu, orders)
            elif choice == 3:
                take_multiple_orders(menu, orders)
            elif choice == 4:
                display_orders(orders)
            elif choice == 5:
                print(f"Total Bill: ${calculate_bill(orders):.2f}")
            elif choice == 6:
                save_orders(orders)
            elif choice == 7:
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")

if __name__ == "__main__":
    main()