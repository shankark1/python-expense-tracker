expenses = []

def show_menu():
    print("\nExpense Tracker")
    print("1. View Expenses")
    print("2. Add Expense")
    print("3. Show Total")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for i, item in enumerate(expenses, start=1):
                print(str(i) + ".", item["name"], "-", item["amount"])

    elif choice == "2":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append({"name": name, "amount": amount})
        print("Expense added.")

    elif choice == "3":
        total = 0
        for item in expenses:
            total += item["amount"]
        print("Total Expense:", total)

    elif choice == "4":
        print("Goodbye")
        break

    else:
        print("Invalid choice.")