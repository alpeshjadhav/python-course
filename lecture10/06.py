class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Worker:
    def __init__(self, company):
        self.company = company

    def display_worker(self):
        print(f"Works at: {self.company}")


class Teacher(Person, Worker):
    def __init__(self, name, age, company, subject):
        Person.__init__(self, name, age)
        Worker.__init__(self, company)
        self.subject = subject

    def display_teacher(self):
        print(f"Teaches: {self.subject}")


t1 = Teacher("Alice", 30, "Greenwood School", "Mathematics")

t1.display_person()   # From Person
t1.display_worker()   # From Worker
t1.display_teacher()  # From Teacher
