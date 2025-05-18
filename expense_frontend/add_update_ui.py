# Import necessary libraries
import streamlit as st  # Streamlit for creating web applications
from datetime import datetime  # For date handling
import requests  # For making HTTP requests to the API

# Define the API endpoint URL (running on localhost port 8000)
API_URL = "http://localhost:8000"


def add_update_tab():
    # Create a date input widget with default value of August 1, 2024
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1))  # Data selection

    # Make a GET request to fetch existing expenses for the selected date
    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    if response.status_code == 200:  # Successful response
        existing_expenses = response.json()   # Get the existing expenses
    else:
        st.error("Failed to retrieve expenses!")

        existing_expenses = []   # Initialize with an empty list if no data retrieved

    # Define available expense categories
    categories = ['Rent', 'Food', 'Shopping', 'Entertainment', 'clothes', 'Other']

    # Create a form container for expense inputs
    with st.form(key="expense_form"):  # Key is used to uniquely identify the form
        # Create column headers for the form
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")  # Header for amount column
        with col2:
            st.text("Category")  # Header for category column
        with col3:
            st.text("Notes")  # Header for note column

        # Initialize an empty list to store expense entries
        expenses = []

        # Create 5 rows of expense inputs
        for i in range(5):
            # If there's existing data for this row, use it
            if i < len(existing_expenses):
                amount = existing_expenses[i]['amount']
                category = existing_expenses[i]['category']
                notes = existing_expenses[i]['notes']
            else:
                # Otherwise use default values
                amount = 0.0
                category = 'Shopping'
                notes = ""

            # Create three columns for each expense row
            col1, col2, col3 = st.columns(3)

            # Amount input in first column
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,  # Pre-filled value
                    key=f"amount_{i}",  # Unique key for each input
                    label_visibility="collapsed"  # Hide the label
                )

            # Category dropdown in second column
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),  # Pre-select existing category
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )

            # Notes text input in third column
            with col3:
                notes_input = st.text_input(
                    label="Notes",
                    value=notes,  # Pre-filled notes
                    key=f"notes_{i}",
                    label_visibility="collapsed"
                )

            # Add this expense entry to our expense list
            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })

        # Create a submitted button for the form
        submit_button = st.form_submit_button()

        # When the form is submitted
        if submit_button:
            # Filter out expenses with zero amounts (these are considered empty)
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]

            # Send a POST request to update expenses for the selected date
            response = requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)

            # Show the appropriate message based on API response
            if response.status_code == 200:
                st.success("Expenses updated successfully!")  # Success message
            else:
                st.error("Failed to update expenses!")   # Error message

