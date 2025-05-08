class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0
        for val in self.marks:
            total += val
        avg = total / 3
        print(f"Hi {self.name}, your avg score is {avg:.2f}")

    @staticmethod
    def collage():
        print("Green Valley School")


s1 = Student("Tony", [88, 76, 90])
s1.get_avg()
Student.collage()
