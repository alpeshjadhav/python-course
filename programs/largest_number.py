num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
num3 = int(input("Enter number3: "))

if num1 == num2 == num3:
    print("All three numbers are equal.")
elif num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number.")
else:
    print(num3, "is the largest number.")
