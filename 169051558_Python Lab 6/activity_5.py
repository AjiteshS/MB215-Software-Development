class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

def compare_car_makes(car1, car2): 
    if car1.make == car2.make:
        return f"{car1} is the same make as {car2}."
    elif car1.make != car2.make:
        return f"{car1} is not the same make as {car2}."
    


if __name__ == "__main__": 
    car1 = Car("Infiniti", "QX60", 2020)
    car2 = Car("Honda", "Pilot", 2022)
    result = compare_car_makes(car1, car2) 
    print(result)  