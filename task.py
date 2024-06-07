import datetime

class Expense:
    def __init__(self, date, amount, description, category):
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_monthly_summary(self, month, year):
        total_expenses = 0
        for expense in self.expenses:
            if expense.date.month == month and expense.date.year == year:
                total_expenses += expense.amount
        return total_expenses

    def get_category_wise_expenditure(self):
        category_wise_expenses = {}
        for expense in self.expenses:
            if expense.category in category_wise_expenses:
                category_wise_expenses[expense.category] += expense.amount
            else:
                category_wise_expenses[expense.category] = expense.amount
        return category_wise_expenses

# Function to display monthly summary
def display_monthly_summary(expense_manager, month, year):
    monthly_summary = expense_manager.get_monthly_summary(month, year)
    print(f"Monthly Summary for {datetime.date(year, month, 1).strftime('%B %Y')}: ${monthly_summary:.2f}")

# Function to display category-wise expenditure
def display_category_wise_expenditure(expense_manager):
    category_wise_expenditure = expense_manager.get_category_wise_expenditure()
    print("Category-wise Expenditure:")
    for category, expenditure in category_wise_expenditure.items():
        print(f"{category}: ${expenditure:.2f}")

# Main function
def main():
    expense_manager = ExpenseManager()

    # User Input
    while True:
        try:
            date_str = input("Enter the date of the expense (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            amount = float(input("Enter the amount spent: $"))
            description = input("Enter a brief description of the expense: ")
            category = input("Enter the category of the expense: ")
            
            # Creating Expense object
            expense = Expense(date, amount, description, category)
            
            # Adding expense to ExpenseManager
            expense_manager.add_expense(expense)
            
            # Ask user if they want to continue adding expenses
            another_expense = input("Do you want to add another expense? (yes/no): ").lower()
            if another_expense != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter valid data.")

    # Data Analysis and User Interface
    print("\nExpense Tracker Menu:")
    print("1. View Monthly Summary")
    print("2. View Category-wise Expenditure")
    choice = input("Enter your choice (1/2): ")
    
    if choice == "1":
        month = int(input("Enter the month (1-12): "))
        year = int(input("Enter the year: "))
        display_monthly_summary(expense_manager, month, year)
    elif choice == "2":
        display_category_wise_expenditure(expense_manager)
    else:
        print("Invalid choice. Exiting...")

main()
