# WAP to find the factorial of n.
n = int(input("Enter number: "))


def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


cal_fact(n)
