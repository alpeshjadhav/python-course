def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


terms = int(input("Enter the number of terms: "))

print("Fibonacci series:")
for i in range(terms+1):
    print(fibo(i), end=" ")
