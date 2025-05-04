nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36

print("Using While Loop")
i = 0
while i < len(nums):
    if nums[i] == x:
        print("Found at index", i)
        break
    else:
        print("Finding...")
    i += 1
else:
    print("Not found in the list.")

print("Using For Loop")
ind = 0
for el in nums:
    if el == x:
        print("Found", ind)
        break
    else:
        print("Finding...")
    ind += 1
else:
    print("END")
