class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self):
        try:
            item_id = int(input("Enter Item ID: "))
            name = input("Enter Item Name: ")
            description = input("Enter Item Description: ")
            price = float(input("Enter Item Price: "))
            
            if price < 0:
                raise ValueError("Price cannot be negative.")
            
            self.items.append(Item(item_id, name, description, price))
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def view_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items:
                print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")

    def update_item(self):
        try:
            item_id = int(input("Enter Item ID to Update: "))
            for item in self.items:
                if item.item_id == item_id:
                    item.name = input("Enter New Name: ")
                    item.description = input("Enter New Description: ")
                    item.price = float(input("Enter New Price: "))
                    print("Item updated successfully!")
                    return
            print("Item not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_item(self):
        try:
            item_id = int(input("Enter Item ID to Delete: "))
            for item in self.items:
                if item.item_id == item_id:
                    self.items.remove(item)
                    print("Item deleted successfully!")
                    return
            print("Item not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def menu(self):
        while True:
            print("\nItem Management Application")
            print("1. Add Item")
            print("2. View Items")
            print("3. Update Item")
            print("4. Delete Item")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_item()
            elif choice == '2':
                self.view_items()
            elif choice == '3':
                self.update_item()
            elif choice == '4':
                self.delete_item()
            elif choice == '5':
                print("Exiting Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ItemManager()
    manager.menu()

