# WAP to find the largest of 4 numbers entered by the user.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

if a >= b and a >= c and a >= d:
    print("A is the largest number:", a)
elif b >= a and b >= c and b >= d:
    print("B is the largest number:", b)
elif c >= a and c >= b and c >= d:
    print("C is the largest number:", c)
else:
    print("D is the largest number:", d)
