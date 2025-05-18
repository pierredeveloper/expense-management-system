import streamlit as st
import requests
from datetime import datetime
import pandas as pd

API_URL = "http://localhost:8000"


def analytics_by_category_tab():
    st.subheader("Expense Breakdown by Category")

    # Define the date range (can be replaced with user input)
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        # Create a dictionary (called payload) to send to the backend API
        payload = {
        # Convert date objects to strings in ISO format (YYYY-MM-DD)
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d")
        }

        # Request analytics data from the backend using string dates
        response = requests.post(f"{API_URL}/analytics_by_category/", json=payload)

        if response.status_code != 200:
            st.error("Failed to fetch data from the server.")
            return

        data = response.json()

        # Prepare empty lists to hold values for displaying in a DataFrame (table)
        categories = []  # Will store expense categories (e.g., Rent, Food)
        totals = []  # Will store total spending per category as formatted strings (e.g., "$120.50")
        percentages = []  # Will store raw percentage values (e.g., 25.34)
        percentages_display = []  # Will store formatted percentage strings (e.g., "25.34%")

        # Loop through the dictionary 'data' returned from the API
        # Each item is in the form: category => {"total": ..., "percentage": ...}
        for category, info in data.items():
            categories.append(category)  # Add category name to list
            totals.append("${:,.2f}".format(info["total"]))  # Format total as dollar string and add
            percentages.append(info["percentage"])  # Add raw percentage value (for charting maybe)
            percentages_display.append(f"{info['percentage']:.2f}%")  # Format percentage for display

        # Create DataFrame with all data
        df = pd.DataFrame({
            "Category": categories,
            "Total": totals,
            "Percentage": percentages,
            "Percentage_Display": percentages_display
        })

        # Sort the DataFrame by Percentage in descending order
        df = df.sort_values(by="Percentage", ascending=False)

        # Display bar chart with sorted values
        st.bar_chart(df.set_index("Category")["Percentage"])

        # Display table with sorted values and formatted percentages
        display_df = df[["Category", "Total", "Percentage_Display"]].rename(columns={
            "Percentage_Display": "Percentage"})
        st.table(display_df)