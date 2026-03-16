class Car1:
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
            print("Error: You cannot drive. The engine is OFF!")
            return False

        print(f"Driving {self.brand} {self.model} in {self.color} color")
        return True

my_car = Car1("Porsche", "Panamera", "burgundy")
my_car.drive()

my_car.start_engine()
success = my_car.drive()
print(f"Drive successful? {success}")