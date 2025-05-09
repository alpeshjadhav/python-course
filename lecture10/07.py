# super()

class Animal:
    def __init__(self, species):
        self.species = species
        print(f"Animal created. Species: {self.species}")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)  # Call parent constructor with species
        self.breed = breed
        print(f"Dog created. Breed: {self.breed}")


d = Dog("Canine", "Labrador")
