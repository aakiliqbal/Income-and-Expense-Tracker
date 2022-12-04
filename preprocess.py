import streamlit as st

incomes = ["Salary","Pocket Money","Other Income"]
expenses = ["Rent","Utilities","Groceries","Trip","Transport","Other Expenses"]
currency = "INR"
page_title = "Income and Expense Tracker"
page_icon = ":moneybag:"
layout = "centered"


def hide_streamlit_style():
    hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
    st.markdown(hide_st_style, unsafe_allow_html=True)


def set_background():
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("https://i.imgur.com/BIJ5o0T.jpg");
        background-size: cover;
        }
        </style>
        """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def set_box_color():
    box_color = """
        <style>
        [data-testid="stVerticalBlock"] {
        background-color: rgb(37, 28, 29);
        border-width: 50px;
        }
        </style>
        """
    st.markdown(box_color, unsafe_allow_html=True)

