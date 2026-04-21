# **🎓 Tutor Lesson & Balance Calculator**

_A lightweight, local management system for private tutors. This application allows you to manage student profiles, 
track lesson history, and automate balance deductions using a Python backend and Streamlit interface._

### **🚀 Key Features**
- Student Management: Add and remove students with customized pricing and payment types (Deposit or Post-pay).
- One-Click Logging: Record lessons instantly; the system automatically calculates the remaining balance based on the 
student's individual rate.
- Balance Tracking: Visual indicators of how many lessons are left or how much is owed.
- Persistent Storage: Uses an SQLite database to ensure your data is saved locally on your machine.

### **🛠️ Tech Stack**
**Language:** Python 3.14
**Framework:** Streamlit (Web Interface)
**Database:** SQLite3
**Architecture:** Modular design with separate layers for Data Management (database.py), 
Data Models (models.py), and UI (app.py).

### **📁 Project Structure**
teacher_calculator/
├── app.py             # Main UI and application logic

├── database.py        # SQL queries and DB connection management

├── models.py          # Data classes (Student/Lesson objects)

└── tutor.db           # SQLite database file (auto-generated)


