a = [[1, 2, 3], [4, 5, 6]]
t = [
    [a[j][i]  # Expression
     for j in range(len(a))]  # Inner loop (row indices)
    for i in range(len(a[0]))  # Outer loop (column indices)
]

for i in t:
    print(i)
