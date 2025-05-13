print("Mini Calculator")

# Input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Menu
print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# User choice
choice = int(input("Enter your choice (1-4): "))

# Perform calculation based on choice
if choice == 1:
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif choice == 2:
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif choice == 3:
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif choice == 4:
    if num2 != 0:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter a number between 1 and 4.")
