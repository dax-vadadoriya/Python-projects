expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        expense = {
            "name": name,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added.")

    elif choice == "2":
        print("\nYour expenses:")

        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. {expense['name']} - ₹{expense['amount']:.2f}"
                )

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print(f"\nTotal expenses: ₹{total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
