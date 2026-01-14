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
            category = input("Enter category: ")
            item = {}
            item['amount'] = amount
            item['category'] = category
            allExpenses.append(item)
            print(f"Added expense: {amount} in category {category}")
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
