a = [[1, 5, 8], [4, 6, 7], [7, 2, 3]]
b = [[4, 5, 6], [8, 9, 1], [3, 5, 6]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]

for row in result:
    print(row)
