# readlines(n) – Reads all lines into a list

with open("read.txt", "r") as f:
    data = f.readlines(10)
    print(data)
