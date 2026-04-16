import streamlit as st
from database import DBManager
from models import Student

st.set_page_config(page_title="TutorCalc", layout="wide")
st.title("🧮 Teacher Calculator")

if "db" not in st.session_state:
    st.session_state.db = DBManager()

db = st.session_state.db

menu = ["Main page", "Add student", "Mark lesson", "Payment"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Main page":
    pass

elif choice == "Add student":
    st.header("Add new student")

    with st.form("add_form"):
        name = st.text_input("Student name")
        price = st.number_input("Student price", min_value=0)
        pay_type = st.selectbox("Pay type", ["deposit", "postpay"])
        balance = st.number_input("Student balance (if it is)", min_value=0)

        submitted = st.form_submit_button("Create")

        if submitted:
            st.session_state.db.add_student(name, price, pay_type, balance)
            st.success(f"Student {name} added successfully!")
