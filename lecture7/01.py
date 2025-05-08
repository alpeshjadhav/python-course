# Functions
def greetings():
    print("Hello..")


greetings()
greetings()
greetings()
print(greetings())  # None


def calc_sum(a, b):
    return a+b


sum = calc_sum(5, 6)
print(sum)


# calculate avg of 3 number
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg


calc_avg(3, 6, 9)

# calculate prod of number


def calc_prod(a, b=5):
    prod = a * b
    print(prod)
    return prod


calc_prod(3)
