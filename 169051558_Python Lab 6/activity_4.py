class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.__model = model  
        self.year = year

    def display_info(self):
        print(f"Car Details: {self.year} {self.make} {self.__model}")

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model
        print(f"Model update: {self.__model}")

    def __str__(self): 
        return f"{self.year} {self.make} {self.__model}"
    
if __name__ == "__main__":
    my_car = Car("Infiniti", "QX60", 2020)
    
    
    print(my_car)  

    my_car.set_model("Q50")  
    print(my_car) 