class ShoppingList:
    def __init__(self):
        self.items = {}

    def add_item(self, category, item):
        if category not in self.items:
            self.items[category] = []
        self.items[category].append(item)
        print(f"{item} has been added to the {category} list.")

    def show_list(self):
        if self.items:
            print("Shopping List:")
            for category, items in self.items.items():
                print(f"\n{category}:")
                for item in items:
                    print(f"- {item}")
        else:
            print("Your shopping list is empty.")


if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        print("\n1. Add Item")
        print("2. Show List")
        print("3. Exit")

        choice = input("Choose an option to proceed: ")

        if choice == "1":
            category = input("What is the category of the item: ")
            item = input("What is the item to be added: ")
            shopping_list.add_item(category, item)
        elif choice == "2":
            shopping_list.show_list()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
