# Finance Accounting

A simple Python console application for tracking personal finances. The program allows users to add income and expenses, view financial records, calculate statistics, and store data in a JSON file.

## Features

* Add income transactions
* Add expense transactions
* Categorize income and expenses
* View all financial records
* Calculate financial statistics
* Validate user input
* Save data to a JSON file
* Load previously saved data when the program starts
* Handle invalid input and exceptions

## Project Structure

```text
finance-accounting/
│
├── main.py
├── categories.py
├── finance.py
├── storage.py
├── data.json
└── README.md
```

### `main.py`

The main program file. It contains the application menu and controls the interaction with the user.

### `categories.py`

Contains predefined categories for income and expenses.

### `finance.py`

Contains functions for validating user input and creating transactions.

### `storage.py`

Responsible for saving financial data to `data.json` and loading it when the application starts.

### `data.json`

Stores income and expense records in JSON format.

## Technologies

* Python 3
* JSON
* File handling
* Functions
* Lists and dictionaries
* Exception handling
* Modular programming

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Clone the repository or download the project files.
3. Open the project folder in a terminal.
4. Run:

```bash
python main.py
```

## Example

After starting the program, the main menu is displayed:

```text
==== FINANCE ACCOUNTING ====

1. ➕ Add Income
2. ➖ Add Expense
3. 📊 View
4. 📈 Statistics
5. ❌ Exit
```

The user can select an option and follow the instructions displayed in the console.

## Data Storage

All financial records are stored locally in `data.json`. The application automatically loads existing data when it starts and saves changes to the file.

Example data structure:

```json
{
    "incomes": [],
    "expenses": []
}
```

## Purpose

This project was created as a Python learning project to practice working with functions, modules, lists, dictionaries, files, JSON, exception handling, and user input.

## Future Improvements

Possible future improvements include:

* Adding a graphical user interface
* Connecting the application to a Telegram bot
* Adding a database such as SQLite
* Adding monthly and yearly reports
* Adding charts and visual statistics
* Adding transaction editing and deletion
* Adding date-based filtering
* Adding an export to CSV feature
* Improving the user interface

## Author

Created as a personal Python learning project.
