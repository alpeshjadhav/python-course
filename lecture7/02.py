# Recursion
def show(n):
    if n == 0:
        return  # base case
    print(n)
    show(n-1)


show(5)


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(5))
