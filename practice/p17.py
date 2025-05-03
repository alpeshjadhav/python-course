# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("enter phy :"))
marks.update({"phy": x})

y = int(input("enter chem :"))
marks.update({"chem": y})

z = int(input("enter bio :"))
marks.update({"bio": z})

print(marks)
