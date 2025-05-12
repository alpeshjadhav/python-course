

# for i in range(1, 100):
#     if i % 13 == 0:
#         print(i)

divisible = int(input("Enter the divisible: "))

myList = [39, 48, 26, 98, 33, 67, 87]

result = list(filter(lambda x: x % divisible == 0, myList))

print(f"The number is divisible by {divisible} is {result}")
