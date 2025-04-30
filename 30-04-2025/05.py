# Tuple Slicing
# Define a tuple
marks = (94, 95, 87, 66, 45)

# Full tuple
print(marks)

# Elements from index 1 to 3 (4 excluded)
print(marks[1:4])  

# First three elements
print(marks[:3])  

# From index 2 to the end
print(marks[2:])  

# Last two elements using negative indexing
print(marks[-2:])  

# Every second element
print(marks[::2])  

# Reversed tuple using slicing
print(marks[::-1])  
