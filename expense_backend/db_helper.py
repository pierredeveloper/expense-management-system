#import logging
import mysql.connector
from contextlib import contextmanager
import os
import sys

# Add the parent directory to sys.path to allow absolute imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Now we can import the logging_setup module
from expense_backend.logging_setup import setup_logger

# Create a custom logger
logger = setup_logger("db_helper") # record messages (like errors, warnings, or info) while your program runs.

@contextmanager  # To open and close files or database connections
def get_db_cursor(commit=False):  # commit=False means “Don’t save changes to the database unless I ask you to.
    """Context manager to manage database connection and cursor."""
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="pierre",
        password="Tala1947**",
        database="expense_manager",
        port="3306"
    )

    # test the connection to the database:
    try:
        if connection.is_connected():
            logger.info("Connection Successful")
        else:
            logger.error("Failed to connect to the database")
            raise Exception("Database connection failed.")

        cursor = connection.cursor(dictionary=True)
        yield cursor

        if commit:
            connection.commit()

    except Exception as e:
        logger.error(f"Error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
        logger.info("Connection closed")

# Fetch all records from expenses table (for testing purposes)
def fetch_all_records():
    logger.info("Fetching all records from the 'expenses' table")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expense_manager.expenses;")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

# Fetch expenses for a specific date
def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expense_manager.expenses WHERE expense_date = %s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

# Insert a new expense
def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense for {expense_date} with amount: {amount}, category: {category}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expense_manager.expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

# Delete expenses for a given date
def delete_expense_for_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expense_manager.expenses WHERE expense_date = %s", (expense_date,))

# Fetch the expense summary for a specific date range
def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetching expense summary from {start_date} to {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) AS total
            FROM expense_manager.expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

# Fetch the analytics data by month
def fetch_analytics_by_month():
    logger.info("Fetching monthly expense analytics.")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT DATE_FORMAT(expense_date, '%Y-%m') AS month, SUM(amount) AS total_expenses
            FROM expense_manager.expenses
            GROUP BY month
            ORDER BY month;
            '''
        )
        data = cursor.fetchall()
        return data


# Test the functions
if __name__ == "__main__":
    expenses = fetch_expenses_for_date("2024-08-01")
    print(expenses)
    #insert_expense("2024-08-20", 40, "Food", "Eat tasty samosa chat")
    #delete_expense_for_date("2024-08-20")
    # summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    # for record in summary:
    #     print(record)
    #fetch_all_records()







