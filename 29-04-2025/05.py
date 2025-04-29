marks = int(input("Enter student marks:"))

if (marks >= 90):
    grade = 'A'
elif (marks >= 70 and marks < 90):
    grade = 'B'
elif (marks >= 50 and marks < 70):
    grade = 'C'
elif (marks >= 35 and marks < 50):
    grade = 'D'
else:
    grade = 'E'

print("Student Grade -> ", grade)
