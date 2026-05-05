import logger_config
import logging
import streamlit as st
from database import DBManager
from datetime import datetime
from models import Student

logger = logging.getLogger(__name__)

st.set_page_config(page_title="TutorCalc", layout="wide")
st.title("🧮 Teacher Calculator")

if "db" not in st.session_state:
    st.session_state.db = DBManager()

db = st.session_state.db

menu = ["Main page", "Add student", "Mark lesson", "Payment", "Settings / Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Main page":
    st.header("📋Current Students")

    students = db.get_all_students()

    if not students:
        st.info("No students yet. Go to 'Add student' page.")
    else:
        for student in students:
            with st.expander(f"👤 Student {student.name}"):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Balance", f"{student.balance}")
                with col2:
                    st.write(f"**Price:** {student.price}")
                    st.write(f"**Pay Type:** {student.pay_type}")
                with col3:
                    if student.pay_type == "deposit":
                        st.write(f"**Lessons left**: {student.get_lessons_left()}")
                    else:
                        st.write(f"**Debt**: {student.calculate_debt()}")

elif choice == "Add student":
    st.header("➕ Add new student")

    name = st.text_input("Student name")
    price = st.number_input("Student price", min_value=0)
    pay_type = st.selectbox("Pay type", ["deposit", "postpay"])
    balance = st.number_input("Student balance (if it is)", min_value=0)

    if st.button("Add student"):
        if name:
            logger.info(f"User is adding a new student: {name}.")
            db.add_student(name, price, pay_type, balance)
            st.success(f"Student {name} added!")
            st.balloons()
            st.rerun()
        else:
            logger.warning("User tried to add a student without a name.")
            st.error("Please enter a name")

elif choice == "Mark lesson":
    st.header("📝 Record a Lesson")
    students = db.get_all_students()
    student_dict = {s.name: s.student_id for s in students}

    selected_name = st.selectbox("Select box", options=student_dict.keys())

    if st.button("Record Lesson"):
        target_id = student_dict[selected_name]

        db.record_lesson(target_id)

        student_data = db.get_student_by_id(target_id)
        current_balance = student_data.balance
        lesson_price = student_data.price

        logging.info(f"Lesson recorded for {selected_name}. ID: {target_id}")

        if current_balance < lesson_price:
            logger.warning(f"Low balance for {selected_name} : {current_balance} left.")
            st.warning(f"Note: {selected_name} has low balance.")

        st.success(f"Lesson {selected_name} recorded!")
        st.rerun()

elif choice == "Payment":
    st.header("💰 Receive Payment")
    students = db.get_all_students()

    if not students:
        st.warning("No students found.")
    else:
        students_dict = {student.name: student for student in students}

        selected_name = st.selectbox("Select a student", options=students_dict.keys())

        chosen_student = students_dict[selected_name]

        if chosen_student.pay_type == "postpay":
            current_debt = chosen_student.calculate_debt()
            st.info(f"Current debt: {current_debt}")
        else:
            st.info(f"Current balance: {chosen_student.balance}")

        amount = st.number_input("Amount Paid", min_value=0.0, step=5.0)

        if st.button("Confirm Payment"):
            logger.info(f"Payment received: {amount} from {selected_name} ({chosen_student.pay_type}).")
            db.debt_paid(
                student_id=chosen_student.student_id,
                amount=amount,
                pay_type=chosen_student.pay_type
            )
            st.success(f"Payment of {amount} for {selected_name} successful!")
            st.balloons()

elif choice == "Settings / Delete":
    st.header("🗑️ Student Management")
    students = db.get_all_students()

    if not students:
        st.info("No students to delete.")
    else:
        students_dict = {f"{s.name} (ID: {s.student_id})": s.student_id for s in students}

        selected_label = st.selectbox("Select student to REMOVE", options=list(students_dict.keys()))

        target_id = students_dict[selected_label]
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes", key="del_yes"):
                logger.warning(f"Student deleted: {selected_label} (ID: {target_id}).")
                db.delete_student(target_id)
                st.toast(f"Student {selected_label} removed!")
                st.rerun()
        with col2:
            if st.button("No", key="del_no"):
                st.info("Action cancelled")
                st.rerun()
