# Creating a list with initial values
my_list = [2, 3, 1]

# Appends 4 to the end of the list
my_list.append(4)
print(my_list)

# Sorts the list in ascending order (modifies in-place, returns None)
print(my_list.sort())
print(my_list)

# Sorts the list in descending order (modifies in-place, returns None)
print(my_list.sort(reverse=True))
print(my_list)

# Inserts the value 5 at index 1
my_list.insert(1, 5)
print(my_list)

# Removes the first occurrence of 5 from the list
my_list.remove(5)
print(my_list)

# Removes the element at index 2
my_list.pop(2)
print(my_list)

# Creating a list of fruits
fruits = ['Apple', 'Pineapple', 'Watermellon', 'Banana', 'Mango', 'Greps']

# Sorts the fruit list alphabetically (modifies in-place)
print(fruits.sort())
print(fruits)

# Sorts the fruit list in reverse alphabetical order
print(fruits.sort(reverse=True))
print(fruits)

# Creating a new list of numbers
numbers = [1, 2, 3, 4, 5]

# Reverses the list in-place
numbers.reverse()
print(numbers)
