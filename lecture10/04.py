class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stoped..")


class ToyotaCar(Car):

    def __init__(self, name):
        super().__init__()
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("SUV")

print(car1.color)
print(car1.start())
