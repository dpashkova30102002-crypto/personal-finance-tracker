from datetime import date

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"Enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def get_valid_amount(prompt: str) -> float:
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            print("Amount must be greater than 0!")
        except ValueError:
            print("Invalid input! Please enter a valid number for amount.")

def display_categories(categories_list: list) -> None:
    print("\nSelect a category:")
    for i, cat in enumerate(categories_list, start=1):
        print(f"{i}. {cat}")

def get_transaction(categories_list: list) -> dict:
    display_categories(categories_list)

    num = get_valid_int(
        prompt=f"Enter a category number (1-{len(categories_list)}): ",
        min_val=1,
        max_val=len(categories_list)
    )

    category_name = categories_list[num - 1]
    amount = get_valid_amount(prompt="Enter amount: ")
    today = date.today().strftime("%d/%m/%Y")

    return {"category": category_name, "amount": amount, "date": today}
