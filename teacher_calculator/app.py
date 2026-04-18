import streamlit as st
from database import DBManager
from datetime import datetime
from models import Student

st.set_page_config(page_title="TutorCalc", layout="wide")
st.title("🧮 Teacher Calculator")

if "db" not in st.session_state:
    st.session_state.db = DBManager()

db = st.session_state.db

menu = ["Main page", "Add student", "Mark lesson", "Payment"]
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

elif choice == "Mark lesson":
    st.header("📝 Record a Lesson")

    students = db.get_all_students()

    if not students:
        st.warning("No students found. Add a student first.")
    else:
        student_dict = {s.name: s.student_id for s in students}
        selected_name = st.selectbox("Select box", options=student_dict.keys())

    if st.button("Lesson Conducted"):
        target_id = student_dict[selected_name]
        db.record_lesson(target_id)
        st.success(f"Lesson for {selected_name} recorded!")

        db.record_lesson(target_id)

        st.success(f"Lesson for {selected_name} recorded!")

elif choice == "Payment":
    pass