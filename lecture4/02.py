# Creating a list of marks
marks = [94, 95, 87, 66, 45]

# Printing the original list
print(marks)

# Slicing from index 1 to 3 (4 is excluded): [95, 87, 66]
print(marks[1:4])

# Slicing from the beginning to index 2 (3 is excluded): [94, 95, 87]
print(marks[:3])

# Slicing from index 1 to the end: [95, 87, 66, 45]
print(marks[1:])

# Negative indexing: from the 3rd last to the 2nd last (excluding last index): [87, 66]
print(marks[-3:-1])
