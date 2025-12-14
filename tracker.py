from typing import Any
from decimal import Decimal
import json
import os


USER_MENU = """
Hi. Please choose number from 1-5 below action on your expenses tracker:
1. Add expense
2. View expenses
3. Total by category
4. Export to CSV
5. Exit
"""

CATEGORY: dict[str, str] = {
    "1": "food",
    "2": "petrol",
    "3": "rental",
}

CATEGORY_PROMPT = "\n".join(f"{k}. {v}" for k, v in sorted(CATEGORY.items()))


def add_expense() -> dict[str, Any]:
    amount = Decimal(input("Please input total amount: "))

    while True:
        category_key = input(f"Please input number:\n{CATEGORY_PROMPT}\n")
        if category_key in CATEGORY:
            break
        print("Invalid category. Please try again.\n")

    event_date = input("Please input the date (YYYY-MM-DD): ")
    description = input("Please input the description: ")

    return {
        "amount": str(amount),
        "category": CATEGORY[category_key],
        "event_date": event_date,
        "description": description,
    }


def view_expenses(file_path: str) -> list[dict[str, str]]:
    if not os.path.exists(file_path):
        return []

    category_input = input(
        f"Please input category number(s):\n{CATEGORY_PROMPT}\n"
        "You may select more than one (example: 1,2): "
    )

    selected_keys = [x.strip() for x in category_input.split(",")]
    valid_categories = [
        CATEGORY[k] for k in selected_keys if k in CATEGORY
    ]

    if not valid_categories:
        print("No valid categories selected.")
        return []

    with open(file_path, "r") as f:
        data = json.load(f)

    filtered_data = [
        obj for obj in data if obj["category"] in valid_categories
    ]

    return filtered_data


def file_processing(file_path: str, row: dict[str, Any]) -> None:
    data: list[dict[str, str]] = []

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)

    data.append(row)

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    action_int = int(input(USER_MENU))

    if action_int == 1:
        row = add_expense()
        file_processing("./data/data.json", row)
        print("Expense added successfully ✅")

    elif action_int == 2:
        expenses = view_expenses("./data/data.json")
        if not expenses:
            print("No expenses found.")
        else:
            for e in expenses:
                print(e)
