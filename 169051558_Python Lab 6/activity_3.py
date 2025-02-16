class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model  
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.__model}")

    def __update_model(self, new_model):
        self.__model = new_model

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model

my_car = Car("Infiniti", "QX60", 2020)
my_car.display_info()  

print(my_car.get_model())  
my_car.set_model("Q50")
my_car.display_info()  



my_car._Car__update_model("G37")
my_car.display_info()  
pass