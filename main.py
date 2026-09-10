from categories import income_categories, expense_categories
from storage import save_data, load_data
from finance import get_valid_int, get_transaction


incomes, expenses = load_data()

while True:
    print("""\n==== FINANCE ACCOUNTING ====
    1. ➕ Add Income
    2. ➖ Add Expense
    3. 📊 View
    4. 📈 Statistics
    5. 💰 Balance
    6. Settings
    7. 🚪 Exit""")

    choice = get_valid_int("Enter your choice(1-7): ", 1, 7)

    match choice:
        case 1:
            transaction = get_transaction(income_categories)
            incomes.append(transaction)
            save_data(incomes, expenses)
            print(f"✅ Income added: {transaction['category']} - {transaction['amount']} - {transaction['date']}")

        case 2:
            transaction = get_transaction(expense_categories)
            expenses.append(transaction)
            save_data(incomes, expenses)
            print(f"✅ Expense added: {transaction['category']} - {transaction['amount']} - {transaction['date']}")

        case 3:
            print("\n===Incomes===")
            if not incomes:
                print("There is no income as yet.")
            else:
                for item in incomes:
                    print(f" - {item['category']}: {item['amount']} | {item['date']}")

            print("\n===Expenses===")
            if not expenses:
                print("There is no expense as yet.")
            else:
                for item in expenses:
                    print(f" - {item['category']}: {item['amount']} | {item['date']}")

        case 4:
            if not incomes and not expenses:
                print("\nNo data available for statistics yet.")
            else:
                print("\n==== STATISTICS ====")

                if expenses:
                    total_exp = sum(item['amount'] for item in expenses)

                    # 1. Групування
                    category_totals = {}
                    for item in expenses:
                        cat = item['category']
                        category_totals[cat] = category_totals.get(cat, 0) + item['amount']

                    # 2. Вивід категорій та відсотків
                    print("\n--- Expenses by Category ---")
                    for cat, amount in category_totals.items():
                        percentage = (amount / total_exp) * 100
                        print(f" • {cat}: {amount:.2f} ({percentage:.1f}%)")

                    # 3. Аналітика
                    high_category = max(category_totals, key=category_totals.get)
                    average_expense = total_exp / len(expenses)

                    print("\n--- Highlights ---")
                    print(f" 🔝 Top Category: {high_category} ({category_totals[high_category]:.2f})")
                    print(f" 📊 Average Expense: {average_expense:.2f}")
                else:
                    print("\nNo expenses recorded yet.")


        case 5:
            total_inc = sum(item['amount'] for item in incomes)
            total_exp = sum(item['amount'] for item in expenses)
            balance = total_inc - total_exp

            print("=== Balance ==="
                  f"\nTotal income: {total_inc}"
                  f"\nTotal expense: {total_exp}"
                  f"\nBalance: {balance}")

        case 6:
            while True:
                print("""\n==== ⚙️ SETTINGS ====
                1. ↩️ Delete last income entry
                2. ↩️ Delete last expense entry
                3. 🧹 Clear all data
                4. ⬅️ Back to Main Menu""")

                sub_choice = get_valid_int("Enter option (1-4): ", 1, 4)

                if sub_choice == 1:
                    if incomes:
                        removed = incomes.pop()
                        save_data(incomes, expenses)
                        print(f"Deleted last income: {removed['category']} - {removed['amount']}")
                    else:
                        print("No income entries to delete!")

                elif sub_choice == 2:
                    if expenses:
                        removed = expenses.pop()
                        save_data(incomes, expenses)
                        print(f"Deleted last expense: {removed['category']} - {removed['amount']}")
                    else:
                        print("No expense entries to delete!")

                elif sub_choice == 3:
                    confirm = input("Are you sure you want to delete ALL data? (yes/no): ").lower().strip()
                    if confirm == "yes":
                        incomes.clear()
                        expenses.clear()
                        save_data(incomes, expenses)
                        print("All transaction data cleared!")
                    else:
                        print("Action cancelled.")

                elif sub_choice == 4:
                    break

        case 7:
            print("Thank you for using! Goodbye 👋")
            break