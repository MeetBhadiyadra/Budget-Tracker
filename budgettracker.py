    import matplotlib.pyplot as plt

class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.expenses = {}
        self.incomes = {}

    def add_expense(self, amount, category):
        self.balance -= amount
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def add_income(self, amount, category):
        self.balance += amount
        if category in self.incomes:
            self.incomes[category] += amount
        else:
            self.incomes[category] = amount

    def view_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        print("Total Income:")
        for category, amount in self.incomes.items():
            print(f"{category}: ₹{amount}")
        print("Total Expenses:")
        for category, amount in self.expenses.items():
            print(f"{category}: ₹{amount}")

    def display_pie_chart(self, data, title):
        labels = data.keys()
        sizes = data.values()
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(title)
        plt.show()

# Main program loop
tracker = BudgetTracker()

while True:
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. Add an income")
    print("3. View balance")
    print("4. Display pie chart of income by category")
    print("5. Display pie chart of expenses by category")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        expense_amount = float(input("Enter the amount of the expense: "))
        expense_category = input("Enter the category of the expense: ")
        tracker.add_expense(expense_amount, expense_category)
        print("Expense added successfully!")
    elif choice == '2':
        income_amount = float(input("Enter the amount of the income: "))
        income_category = input("Enter the category of the income: ")
        tracker.add_income(income_amount, income_category)
        print("Income added successfully!")
    elif choice == '3':
        tracker.view_balance()
    elif choice == '4':
        tracker.display_pie_chart(tracker.incomes, "Income by Category")
    elif choice == '5':
        tracker.display_pie_chart(tracker.expenses, "Expenses by Category")
    elif choice == '6':
        print("Exiting budget tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
