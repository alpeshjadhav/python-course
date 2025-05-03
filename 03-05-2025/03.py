# Creating a set
mySet = {1, 2, 3, 4, 5, 6, "hello", "python", 4, 6}

print(mySet)              # Print the set (duplicates removed)
print(type(mySet))        # Check the data type
print(len(mySet))         # Length of the set (unique elements only)

# Creating an empty set using set() constructor
newSet = set()

print(newSet)             # Empty set

# Adding elements to the set
newSet.add(1)
newSet.add(2)
newSet.add(2)             # Duplicate, will be ignored
newSet.add(3)

print(newSet)             # {1, 2, 3}

# Removing an element
newSet.remove(2)          # Removes 2 from the set
# newSet.remove(6)        # Would raise KeyError since 6 is not in the set

print(newSet)             # {1, 3}

# Adding a string and a tuple to the set
newSet.add("hi")
newSet.add((1, 2, 3, 4, 5))  # Tuples are immutable, so allowed in sets

print(newSet)             # Set with mixed elements
print(len(newSet))        # Number of unique elements

# Clearing the set
newSet.clear()

print(len(newSet))        # Set is now empty

# Set of fruits
fruits = {"apple", "banana", "cherry", "mango", "pineapple"}

print(fruits)

# Remove a random item from the set
fruits.pop()

print(fruits)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)              # Union
print(a & b)              # Intersection
print(a - b)              # Difference
print(a ^ b)              # Symmetric Difference

# Same operations using set methods
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
