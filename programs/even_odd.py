num = int(input("Enter a number: "))

if num == 1:
    print("Natural number and Odd number")
elif num > 1:
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Not a natural number")
