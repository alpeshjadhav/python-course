num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}")
