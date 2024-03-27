class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity, unit_price):
        self.items.append({
            "item": item,
            "quantity": quantity,
            "unit_price": unit_price
        })
        print(f"{quantity} {item}(s) added to the list for $ {unit_price} each.")

    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items)
        return total

    def show_list(self):
        if self.items:
            print("Shopping List:")
            for item in self.items:
                print(f"{item['quantity']} {item['item']}(s) - $ {item['unit_price']} each")
            print("Total: $", self.calculate_total())
        else:
            print("Your shopping list is empty.")


if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        print("\n1. Add Item")
        print("2. Show List")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            item = input("What is the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            unit_price = float(input("Enter the unit price: "))
            shopping_list.add_item(item, quantity, unit_price)
        elif choice == "2":
            shopping_list.show_list()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
