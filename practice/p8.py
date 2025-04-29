# WAP to find the greatest of 3 numbers entered by the user.

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a >= b and a >= c:
    print("A is the greatest number:", a)
elif b >= a and b >= c:
    print("B is the greatest number:", b)
else:
    print("C is the greatest number:", c)
