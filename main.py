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