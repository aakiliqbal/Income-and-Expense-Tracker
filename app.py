import calendar
import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime

#Importing local files
import helper
import mongodb as mdb
import preprocess as pp


#Settings
st.set_page_config(page_title=pp.page_title, page_icon=pp.page_icon,layout=pp.layout)
st.title(pp.page_icon + " " + pp.page_title + " " + pp.page_icon)

#Hide streamlit style
pp.hide_streamlit_style()
pp.set_background()
pp.set_box_color()


#Navigation menu
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],  
    orientation="horizontal",
    )


#Drop down values
years = [datetime.today().year,datetime.today().year + 1]
months = list(calendar.month_name[1:])

#Input for fields

if selected == "Data Entry":
    st.header(f"Data Entry in {pp.currency}")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        col1.selectbox("Select Month:", months, key="month")
        col2.selectbox("Select Year:", years, key="year")

        "---"
        with st.expander("Income"):
            for income in pp.incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in pp.expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment here ...")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = str(st.session_state["year"]) + "_" + str(st.session_state["month"])
            incomes = {income: st.session_state[income] for income in pp.incomes}
            expenses = {expense: st.session_state[expense] for expense in pp.expenses}

            mdb.insert_period(period, incomes, expenses, comment)
            
            st.success("Data saved!")

#Plotting Periods
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", mdb.fetch_all_periods())
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # Get data from database
            period_data = mdb.get_period(period)
            comment = period_data.get("comment")
            expenses = period_data.get("expenses")
            incomes = period_data.get("incomes")

            # Create metrics
            total_income = sum(incomes.values())
            total_expense = sum(expenses.values())
            remaining_budget = total_income - total_expense
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Income", f"{total_income} {pp.currency}")
            col2.metric("Total Expense", f"{total_expense} {pp.currency}")
            col3.metric("Remaining Budget", f"{remaining_budget} {pp.currency}")
            st.text(f"Comment: {comment}")

            "---"
            #Plot pie chart
            helper.plot_pie_chart(expenses,remaining_budget)
            #Plot sankey chart
            helper.plot_sankey_chart(expenses,incomes)
            #plot bar chart
            helper.plot_bar_chart(expenses)

            


