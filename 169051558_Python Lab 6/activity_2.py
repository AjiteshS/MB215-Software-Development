class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

my_car = Car("Infiniti", "QX60", 2020)
print(my_car.make)  
print(my_car.model)  
print(my_car.year)   

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

    def __update_model(self, new_model):
        self.model = new_model

my_car = Car("Infiniti", "QX60", 2020)
my_car.display_info()  

my_car._Car__update_model("Q50")  
my_car.display_info()  