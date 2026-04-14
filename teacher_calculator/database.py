import sqlite3
from datetime import datetime
from models import Student

class DBManager:
    def __init__(self, db_path="tutor.db"):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            pay_type TEXT NOT NULL,
            balance REAL DEFAULT 0
        )
    """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        lesson_date TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
        )
    """)
        self.connection.commit()

    def add_student(self, name, price, pay_type, balance=0):
        sql_query = """
        INSERT INTO students (name, price, pay_type, balance)
        VALUES (?, ?, ?, ?)
        """
        data = (name, price, pay_type, balance)
        self.cursor.execute(sql_query, data)
        self.connection.commit()

    def record_lesson(self, student_id):
        now = datetime.now()
        today_date = now.strftime("%Y-%m-%d")

        sql_query1 = "INSERT INTO lessons (student_id, lesson_date) VALUES (?, ?)"
        data1 = (student_id, today_date)
        self.cursor.execute(sql_query1, data1)
        self.connection.commit()

        sql_query2 = """
        UPDATE students
        SET balance = balance - price
        WHERE student_id = ? AND pay_type = "deposit"
        """
        data2 = (student_id,)
        self.cursor.execute(sql_query2, data2)
        self.connection.commit()

    def get_all_students(self):
        sql = "SELECT id, name, price, pay_type, balance FROM students"
        self.cursor.execute(sql)

        rows = self.cursor.fetchall()

        students_objects = []

        for row in rows:
            lessons_amount = self.count_lessons(row[0])

            new_student = Student(
                student_id = row[0],
                name = row[1],
                price = row[2],
                pay_type = row[3],
                balance = row[4],
                lessons_had = lessons_amount
            )

            students_objects.append(new_student)

        return students_objects

    def count_lessons(self, student_id):
        sql = "SELECT COUNT(*) FROM lessons WHERE student_id = ?"
        self.cursor.execute(sql, (student_id,))
        result = self.cursor.fetchone()
        return result[0]

    def delete_student(self, student_id):


    def execute_query(self):
        pass

    def fetch_students(self):
        pass

    def fetch_lessons(self):
        pass

