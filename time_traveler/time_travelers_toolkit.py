import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

current_year = dt.datetime.today()
current_time = dt.datetime.now().time()

print(current_year.strftime("It is %d.%m.%Y today"))
print(current_time.strftime("It is %H:%M:%S now"))

def calculate_time_travel_cost(current_year, target_year):
    base_cost = Decimal("1000.0")

    year_diff = abs(target_year - current_year)

    cost_per_year = Decimal("15.5")

    total_cost = base_cost + (Decimal(str(year_diff)) * cost_per_year)

    return f"{total_cost:.2f}"

target_year = randint(1000, 3000)
final_cost = calculate_time_travel_cost(2026, target_year)

destinations = ["Rome", "Japan", "Mars Colony", "London", "Milky Way"]
selected_destination = choice(destinations)

message = custom_module.generate_time_travel_message(
       target_year,
       selected_destination,
       final_cost
   )

print(message)