print("Basic while loop")
count = 1
while count <= 5:
    print("hello")
    count += 1
print(count)

print("\nUsing continue to skip value 3")
i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue
    print(i)
    i += 1

print("\nPrint only odd numbers between 0 and 10")
i = 0
while i <= 10:
    if (i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1
