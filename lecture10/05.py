class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped..")


class ToyotaCar(Car):
    def __init__(self, brand):
        super().__init__()
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type


car1 = Fortuner("Fortuner", "Petrol")

print(car1.color)        # from Car
print(car1.brand)        # from ToyotaCar
print(car1.fuel_type)    # from Fortuner

car1.start()             # static method from Car
