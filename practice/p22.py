# Print the elements of the following list using a loop.
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0

print("Using While Loop...")

while i < len(nums):
    print(nums[i])
    i += 1

print("Using For Loop...")

for el in nums:
    print(el)
