import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "date": date,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!\n")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.\n")
        return

    print("\n--- Expense Records ---")

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense #{index}")
        print(f"Date: {expense['date']}")
        print(f"Category: {expense['category']}")
        print(f"Amount: ₹{expense['amount']}")


def search_expense(expenses):
    category = input("Enter category to search: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            print("\nExpense Found!")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: ₹{expense['amount']}")
            found = True

    if not found:
        print("\nNo matching expenses found.\n")


def delete_expense(expenses):
    category = input("Enter category to delete: ")

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            expenses.remove(expense)
            save_expenses(expenses)

            print("\nExpense deleted successfully!\n")
            return

    print("\nExpense not found.\n")


def show_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ₹{total}\n")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Delete Expense")
        print("5. Show Total Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            search_expense(expenses)

        elif choice == "4":
            delete_expense(expenses)

        elif choice == "5":
            show_total(expenses)

        elif choice == "6":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice!\n")


if __name__ == "__main__":
    main()
    