lower = int(input("enter a lower number: "))
upper = int(input("enter a upper number: "))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
