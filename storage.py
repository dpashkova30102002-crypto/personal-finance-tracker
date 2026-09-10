import json
import os

FILE_NAME = "data.json"

def save_data(incomes: list, expenses: list) -> None:
    data ={
        "incomes": incomes,
        "expenses": expenses
    }
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        print("Data saved successfully!")

def load_data() -> tuple[list, list]:
    if not os.path.exists(FILE_NAME):
        return [], []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("incomes", []), data.get("expenses", [])
    except (json.JSONDecodeError, Exception):
        print("Failed to load saved data. Starting with empty tracker.")
        return [], []