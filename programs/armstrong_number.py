num = int(input("Enter a number: "))
order = len(str(num))

armstrong_sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** order
    temp //= 10

if armstrong_sum == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
