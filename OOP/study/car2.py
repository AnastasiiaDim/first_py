class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

        self.is_engine_on = False

    def start_engine(self):
        self.is_engine_on = True
        print("Engine started. VROOM!")

    def drive(self):
        if not self.is_engine_on:
            return "Error: You cannot drive. The engine is OFF!"

        return f"Driving {self.brand} {self.model} in {self.color} color"

my_car = Car("Porsche", "Panamera", "burgundy")
my_car.drive()

my_car.start_engine()
success = my_car.drive()
print(f"Drive successful? {success}")