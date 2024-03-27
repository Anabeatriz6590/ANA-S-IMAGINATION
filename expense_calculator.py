class ExpensesCalculator:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, value):
        if category not in self.expenses:
            self.expenses[category] = []
        self.expenses[category].append(value)
        print(f"Expense of ${value} in category '{category}' added successfully.")

    def calculate_category_total(self, category):
        if category in self.expenses:
            total = sum(self.expenses[category])
            return total
        else:
            return 0

    def calculate_overall_total(self):
        total = sum(sum(values) for values in self.expenses.values())
        return total


if __name__ == "__main__":
    calculator = ExpensesCalculator()

    while True:
        print("\n1. Add Expense")
        print("2. Calculate Total by Category")
        print("3. Calculate Overall Total")
        print("4. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            category = input("Enter the expense category: ").upper()
            value = float(input("Enter the expense amount: "))
            calculator.add_expense(category, value)
        elif choice == "2":
            category = input("Enter the category to calculate the total: ").upper()
            total_category = calculator.calculate_category_total(category)
            print(f"Total expenses in category '{category}': ${total_category}")
        elif choice == "3":
            total_overall = calculator.calculate_overall_total()
            print(f"Overall total expenses: ${total_overall}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
