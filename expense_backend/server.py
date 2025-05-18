from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
import db_helper
from pydantic import BaseModel
import logging

# Initialize FastAPI app
app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the data model for an expense entry
class Expense(BaseModel):
    #expense_date: date
    amount: float
    category: str
    notes: str

# Define the data model for specifying a date range
class DateRange(BaseModel):
    start_date: date
    end_date: date

# Response model for monthly expenses
class MonthlyExpense(BaseModel):
    month: str
    total_expenses: float

# Endpoint to get expenses for a specific date
@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    try:
        # Fetch expenses from the database for the given date
        expenses = db_helper.fetch_expenses_for_date(expense_date)

        # If no data is retrieved, raise a 404 error
        if not expenses:
            raise HTTPException(status_code=404, detail="No expenses found for the given date")

        # Return the list of retrieved expenses
        return expenses

    except Exception as e:
        logger.error(f"Error fetching expenses: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# Endpoint to add or update expenses for a specific date
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    try:
        # First, delete any existing expenses for the given date to avoid duplicates
        db_helper.delete_expense_for_date(expense_date)

        # Iterate over the list of incoming expenses
        for expense in expenses:
            # Insert each expense into the database with the provided details
            db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

        # Return a success message after all expenses have been inserted
        return {"message": "Expenses updated successfully"}

    except Exception as e:
        logger.error(f"Error adding or updating expenses: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Endpoint to get expense analytics for a specific date range
@app.post("/analytics_by_category/")  # Post request Endpoint
def get_analytics(date_range: DateRange):  # function to calculate analytics or summaries based on a range of dates
    try:
        # Fetch expense summary data from the database within the given date range
        data = db_helper.fetch_expense_summary(date_range.start_date, date_range.end_date)

        # If no data is retrieved, raise a 404 error
        if not data:
            raise HTTPException(status_code=404, detail="No expense data found for the given date range")

        # Calculate the total amount of all expenses
        total = sum([row['total'] for row in data])

        # Initialize a dictionary to store breakdown of expenses by category
        breakdown = {}

        # Iterate through each expense record
        for row in data:
            # Calculate the percentage of the total expense for each category
            percentage = round((row['total'] / total) * 100 if total != 0 else 0, 2)

            # Add the total and percentage for each category to the breakdown dictionary
            breakdown[row['category']] = {
                "total": row['total'],
                "percentage": percentage
            }

        # Return the breakdown dictionary as the response
        return breakdown

    except Exception as e:
        logger.error(f"Error fetching analytics: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


# Endpoint to get analytics by month
@app.get("/analytics_by_month/", response_model=List[MonthlyExpense])
def get_expenses_by_month():  # function that group expenses by month
    try:
        data = db_helper.fetch_analytics_by_month()

        # If no data is retrieved, raise a 404 error
        if not data:
            raise HTTPException(status_code=404, detail="No expense data found by month")

        # Transform database rows into a list of MonthlyExpense objects
        expenses_by_month = [
            MonthlyExpense(month=row['month'], total_expenses=row['total_expenses'])
            for row in data
        ]

        return expenses_by_month

    except Exception as e:
        logger.error(f"Error fetching monthly analytics: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")










