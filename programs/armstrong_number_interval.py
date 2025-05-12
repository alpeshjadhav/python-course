lower = int(input("Enter a number: "))
upper = int(input("Enter a number: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    temp = num
    armstrong_sum = 0
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** order
        temp //= 10

    if armstrong_sum == num:
        print(f"{num} is an Armstrong number.")
else:
    print("End")
