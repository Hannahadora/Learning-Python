from datetime import date


def expenseTrackerCalc():
    print("Welcome to the Expense Tracker!")
    command = input("Enter a command (add, view, exit): ")
    allExpenses = []
    while command != "exit":
        if command == "add":
            amount = input("Enter amount: ")
            if not amount.replace('.', '', 1).isdigit():
                print("Invalid amount. Please enter a numeric value.")
                continue
            if not amount:
                print("Amount cannot be empty.")
                continue
            category = input("Enter category: ")
            if not category:
                print("Category cannot be empty.")
                continue
            date = input("Enter date (YYYY-MM-DD): ")
            if not date:
                print(f"Date will be set to today's date.")
                date = date.today()
                continue
            item = {}
            item['amount'] = amount
            item['category'] = category
            item['date'] = date
            allExpenses.append(item)
            print(f"Added expense: {amount} in category {category} on {date}")
        elif command == "view":
            for expense in allExpenses:
                totalExpenseAmount = sum(float(expense['amount']) for expense in allExpenses)
                print(f"Expense: {expense['amount']} -> Category: {expense['category']}")
            print(f"Total Expense Amount: {totalExpenseAmount}")
        else:
            print("Unknown command.")
        command = input("Enter a command (add, view, exit): ")
    print("Exiting Expense Tracker. Goodbye!")

if __name__ == "__main__":
    expenseTrackerCalc()
