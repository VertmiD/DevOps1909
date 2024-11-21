class Car:
    def __init__(self, company, model, year, color):
        self.company = company
        self.model = model
        self.year = year
        self.color = color

speed = 120
color = "red"
my_car = Car("Toyota", "Corolla", 2020, "white")
print(f"The {my_car.company} {my_car.model} from {my_car.year} in color {my_car.color} is accelerating to {speed} KM/h")

my_car.company = "Honda"
my_car.model = "Civic"
my_car.year = 2018
my_car.color = "Blue"

print(f"My updated car is a {my_car.color} {my_car.company} {my_car.model} from {my_car.year}")
