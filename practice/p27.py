# WAP to find the factorial of n number.

n = int(input("Enter Number: "))

# Using while loop
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial using while loop =", fact)

# Using for loop
fact = 1
for i in range(1, n + 1):
    fact *= i
else:
    print("Factorial using for loop =", fact)
