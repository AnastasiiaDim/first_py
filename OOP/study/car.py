class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        return f"Driving {self.brand} {self.model} in {self.color} color"

car1 = Car("BMW", "X5", "green")
print(car1.drive())
