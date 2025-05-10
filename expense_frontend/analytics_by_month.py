import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Base URL for API calls
API_URL = "http://localhost:8000"


def analytics_by_month_tab():
    """
    Function to generate and display the monthly expense analysis tab
    Retrieves monthly expense data, processes it, and displays it in both chart and table format
    """
    # Create a subheader for this section
    st.subheader("Expense Breakdown By Months")

    # Try to fetch data from the server, handle any connection errors
    try:
        # Make GET request to the monthly analytics endpoint
        data = requests.get(f"{API_URL}/analytics_by_month/").json()
    except:
        # Display error message if the request fails
        st.error("Failed to retrieve data from the server")
        return

    # Check if any data was returned
    if not data:
        # Show warning if no data is available
        st.warning("No data available.")
        return

    # Convert the JSON response to a pandas DataFrame
    df = pd.DataFrame(data)

    # Convert the 'month' column to datetime format for proper sorting
    df["Month"] = pd.to_datetime(df["month"], format="%Y-%m")

    # Extract the month name (e.g., "January") from the datetime object
    df["Month Name"] = df["Month"].dt.strftime("%B")

    # Sort the DataFrame chronologically by month
    df = df.sort_values("Month")

    # Create a bar chart of monthly expenses
    # Use the month names as x-axis labels and total expenses as y-axis values
    st.bar_chart(df.set_index("Month Name")["total_expenses"], use_container_width=True)

    # Format the expense amounts as dollar values with commas and 2 decimal places
    df["total_expenses"] = df["total_expenses"].map("${:,.2f}".format)

    # Display a table showing the formatted expense totals by month
    st.table(df.set_index("Month Name")[["total_expenses"]])








