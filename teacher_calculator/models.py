class Student:
    def __init__(self, student_id, name, price, pay_type, balance, lessons_had):
        if price <= 0:
            raise ZeroDivisionError("Price cannot be negative")
        self.student_id = student_id
        self.name = name
        self.price = price
        self.pay_type = pay_type
        self.balance = balance
        self.lessons_had = lessons_had

    def get_lessons_left(self):
        if self.pay_type == "deposit":
            return round(self.balance / self.price, 1)
        else:
            return 0

    def calculate_debt(self):
        if self.pay_type == "postpay":
            return self.lessons_had * self.price
        else:
            return 0

    def __str__(self):
        text = f"Student name: {self.name} || Type: {self.pay_type}"
        if self.pay_type == "deposit":
            text += f" | Lessons left: {self.get_lessons_left()}"
        else:
            text += f" | To pay: {self.calculate_debt()}"

        return text


