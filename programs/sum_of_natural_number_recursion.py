def natural_number_sum(n):
    if n <= 1:
        return n
    else:
        return natural_number_sum(n-1) + n


num = int(input("Enter a number here: "))

if num <= 0:
    print("Enter a positive number")
else:
    print(natural_number_sum(num))
