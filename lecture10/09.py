class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"


stud1 = Student(96, 92, 85)
print(stud1.percentage)

stud1.phy = 86
print(stud1.percentage)
