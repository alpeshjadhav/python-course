# WAP to find the sum of first natural numbers.

n = 5
sum = 0

print("Using For loop")
for i in range(1, n + 1):
    sum += i

print(sum)

print("Using While Loop")
i = 0
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)
