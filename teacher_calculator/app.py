import streamlit as st
from teacher_calculator.database import DBManager

st.title("Teacher Calculator")
db = DBManager()