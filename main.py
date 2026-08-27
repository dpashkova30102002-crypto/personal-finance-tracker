incomes = []
expenses = []
income_categories = [
    "Salary (main job)",
    "Freelance / Projects (side jobs, gigs)",
    "Investments & Interest (deposits, stocks, cashback)",
    "Gifts / Transfers (money from relatives/friends)",
    "Selling items (used goods, property)",
    "Other (casual income)"
]

expense_categories = [
    "Groceries & Food (supermarkets, local markets)",
    "Cafes & Restaurants (coffee, delivery, dining out)",
    "Transportation (fuel, public transit, taxi, car maintenance)",
    "Housing & Utilities (rent, utilities, internet)",
    "Shopping & Clothing (electronics, clothes, home items)",
    "Health & Fitness (pharmacies, doctors, gym)",
    "Entertainment & Leisure (movies, hobbies, subscriptions)",
    "Education & Growth (courses, books)",
    "Gifts & Donations (holidays, charity)",
    "Other / Unforeseen (miscellaneous expenses)"
]


def get_transaction(categories_list):
    print("\nSelect a category:")
    for i, cat in enumerate(categories_list, start=1):
        print(f"{i}. {cat}")

    while True:
        try:
            num = int(input(f"Enter a category number (1-{len(categories_list)}): "))
            if 1 <= num <= len(categories_list):
                break
            else:
                print(f"Invalid number! Please enter a number between 1 and {len(categories_list)}.")
        except ValueError:
            print(f"Invalid number! Please enter a number between 1 and {len(categories_list)}.")


    category_name = categories_list[num - 1]
    amount = float(input("Enter amount: "))

    return {"category": category_name, "amount": amount}

while True:
    print("""\n==== FINANCE ACCOUNTING ====
    1. ➕ Add Income
    2. ➖ Add Expense
    3. 📊 View
    4. 📈 Statistics
    5. 💰 Balance
    6. 🏦 Savings
    7. 🚪 Exit""")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number from 1 to 7.")
        continue

    match choice:
        case 1:
            transaction = get_transaction(income_categories)
            incomes.append(transaction)
            print(f"✅ Income added: {transaction['category']} - {transaction['amount']}")

        case 2:
            transaction = get_transaction(expense_categories)
            expenses.append(transaction)
            print(f"✅ Expense added: {transaction['category']} - {transaction['amount']}")

        case 3:
            print("\n===Incomes===")
            if not incomes:
                print("There is no income as yet.")
            else:
                for item in incomes:
                    print(f" - {item['category']}: {item['amount']}")

            print("\n===Expenses===")
            if not expenses:
                print("There is no expense as yet.")
            else:
                for item in expenses:
                    print(f" - {item['category']}: {item['amount']}")
                    
        case 4:
            print("In development")


        case 5:
            total_inc = sum(item['amount'] for item in incomes)
            total_exp = sum(item['amount'] for item in expenses)
            balance = total_inc - total_exp

            print("=== Balance ==="
                  f"\nTotal income: {total_inc}"
                  f"\nTotal expense: {total_exp}"
                  f"\nBalance: {balance}")

        case 7:
            print("Thank you for using! Goodbye 👋")
            break

        case _:
            print("This feature is not yet available or you have selected the wrong item.")