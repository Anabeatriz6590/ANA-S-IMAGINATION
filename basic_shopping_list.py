class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} has been added to the list.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} has been removed from your list.")
        else:
            print(f"{item} is not in your list.")

    def show_list(self):
        if self.items:
            print("----Shopping List----")
            for item in self.items:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")


if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        print("\n1. Add New Item")
        print("2. Remove Item")
        print("3. Show List")
        print("4. Exit")

        choice = input("Choose an option to proceed: ")

        if choice == "1":
            item = input("Enter the item to be added: ")
            shopping_list.add_item(item)
        elif choice == "2":
            item = input("Enter the item to be removed: ")
            shopping_list.remove_item(item)
        elif choice == "3":
            shopping_list.show_list()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
