import os
import sys
import pytest

# Add the project root to the Python path
# This assumes test_db_helper.py is in tests/backend/ directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
if project_root not in sys.path:
    sys.path.append(project_root)

# Now you can import your module
from expense_backend import db_helper

def test_fetch_expenses_for_date_aug_15():
    expenses = db_helper.fetch_expenses_for_date("2024-08-08")
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 35.0
    assert expenses[0]['category'] == "Entertainment"
    assert expenses[0]['notes'] == "Go to cinema"

def test_fetch_expenses_for_date_invalid_date():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")
    assert len(expenses) == 0

def test_fetch_expenses_summary_invalid_date_range():
    expenses = db_helper.fetch_expense_summary("9999-08-01", "9999-12-31")
    assert len(expenses) == 0








