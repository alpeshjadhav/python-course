number = int(input("Enter number of terms: "))
a, b = 0, 1

if number <= 0:
    print("Please enter a positive number")
elif number == 1:
    print(a)
else:
    print(a)
    print(b)
    for _ in range(2, number):
        c = a + b
        print(c)
        a, b = b, c
