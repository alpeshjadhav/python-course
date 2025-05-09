# @classmethod

class Employee:
    raise_percent = 1.05  # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percent)

    @classmethod
    def set_raise_percent(cls, new_percent):
        cls.raise_percent = new_percent


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

Employee.set_raise_percent(1.10)  # Change class variable using class method

e1.apply_raise()
e2.apply_raise()

print(e1.salary)  # 55000
print(e2.salary)  # 66000
