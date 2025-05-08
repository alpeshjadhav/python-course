class Student:
    # Class Attribute
    collage_name = "Green Valley School"

    # Constructor with instance attributes
    def __init__(self, name="Unknown", marks=0):
        self.name = name
        self.marks = marks
        print(f"Adding student: {self.name}, Marks: {self.marks}")

    # Instance method to display details
    def display(self):
        print(
            f"Name: {self.name}, Marks: {self.marks}, School: {Student.collage_name}")


# Creating objects
s1 = Student("Alpesh", 79)
s2 = Student("Nandini", 91)
s3 = Student()

# Displaying info
s1.display()
s2.display()
s3.display()

# Changing class attribute (affects all instances)
Student.collage_name = "New Horizon School"
print("\nAfter changing school name:\n")
s1.display()
s2.display()
s3.display()
