num = int(input("Enter a number: "))

# solution 1: Using for loop
print("Using for loop")
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")

# solution 2: Using while loop
print("\n\nUsing while loop")
i = 1
while i <= 10:
    result = num * i
    print(f"{num} * {i} = {result}")
    i += 1
