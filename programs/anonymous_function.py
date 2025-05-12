nTerms = int(input("enter number of terms here:"))

result = list(map(lambda x: 2 ** x, range(nTerms+1)))

for i in range(nTerms+1):
    print(f"The value of 2 raised to power {i} is {result[i]}")
