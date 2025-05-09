class Person:
    __name = "anonymous"  # private class variable

    def __hello(self):    # private instance method
        print("Hellllooooo")

    def welcome(self):    # public instance method
        self.__hello()


p1 = Person()

print(p1.welcome())
