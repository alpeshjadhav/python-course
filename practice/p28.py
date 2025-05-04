# Find Factorial of First n Numbers

n = int(input("Enter Number: "))

# Using while loop
print("Using while loop:")
i = 1
while i <= n:
    fact = 1
    j = 1
    while j <= i:
        fact *= j
        j += 1
    print(f"{i}! = {fact}")
    i += 1

# Using for loop
print("\nUsing for loop:")
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    print(f"{i}! = {fact}")
