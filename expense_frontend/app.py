import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_by_category_tab
from analytics_by_month import analytics_by_month_tab

st.title("Expense Tracking System")

tab1, tab2, tab3 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Month"])

# Create tab1 "Add/Update"
with tab1:
    add_update_tab()

# Create tab1 "Analytics By Category"
with tab2:
    analytics_by_category_tab()

# Create tab1 "Analytics By Month"
with tab3:
    analytics_by_month_tab()


