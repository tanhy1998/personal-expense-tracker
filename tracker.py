from dataclasses import dataclass, field
from enum import Enum, auto, StrEnum
from decimal import Decimal
from datetime import datetime


USER_MENU = """
Hi. Please choose number from 1-5 below action on your expenses tracker:
1. Add expense
2. View expenses
3. Total by category
4. Export to CSV
5. Exit
"""

class category(StrEnum):
    food = auto()
    petrol = auto()
    rental = auto()

@dataclass
class Expenses():
    amount: Decimal
    category: category 
    date: datetime
    description: str = ""

    def add_expenses(self)
