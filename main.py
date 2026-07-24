class Expenses:
    pass


class ExpenseTracker:
    def __init__(self):
        self.expenses = []


    def add_expense(self, expense):
        self.expenses.append(expense)


    def show_expense(self):
        if len(self.expenses) == 0:
            print("No expense found")
            return
        for expense in self.expenses:
            print(expense.name, expense.amount)


    def delete_expense(self, expense):
        try:
            self.expenses.remove(expense)
            return True
        except ValueError:
            return 


    def search_expense(self, name):
        for expense in self.expenses:
            if expense.name == name:
                return expense

        return None



    def update_expense(self, name, amount):
        expense = self.search_expense(name)

        if expense is None:
            return True

        expense.amount = amount
        return True



tracker = ExpenseTracker()

running = True
while running:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Show Expense")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Exit")

    try:
        choice = int(input("Choose an option:  "))
    except ValueError:
        print("Invalid input: Please, only digits are allowed.")
        continue
    if choice == 1:
        tracker.add_expense()

    if choice == 2:
        tracker.show_expense()

    if choice == 3:
        tracker.search_expense()

    if choice == 4:
        tracker.update_expense()

    if choice == 5:
        tracker.delete_expense()

    if choice == 6:
        running = False

