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
        # Convert date objects to strings in ISO format (YYYY-MM-DD)
        payload = {
            'start_date': start_date.strftime("%Y-%m-%d"),
            'end_date': end_date.strftime("%Y-%m-%d")
        }

        # Request analytics data from the backend using string dates
        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("Failed to fetch data from the server.")
            return

        data = response.json()

        # Convert JSON response to DataFrame
        categories = []
        totals = []
        percentages = []
        percentages_display = []

        for category, info in data.items():
            categories.append(category)
            totals.append("${:,.2f}".format(info["total"]))
            percentages.append(info["percentage"])
            percentages_display.append(f"{info['percentage']:.2f}%")

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