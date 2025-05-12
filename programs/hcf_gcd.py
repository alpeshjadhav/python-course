# Highest Common Factor = HCF
# Greatest Common Divisor = GCD

def find_HCF(x, y):
    hcf = 1
    smaller = min(x, y)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


def find_GCD(a, b):
    while b:
        a, b = b, a % b
    return a


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("The HCF of the given two numbers is", find_HCF(num1, num2))
    print("The GCD of the given two numbers is", find_GCD(num1, num2))

except ValueError:
    print("Please enter valid integers.")
