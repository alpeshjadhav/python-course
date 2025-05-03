student = {
    "name": "Rahul Kumar",
    "subjects": {
        "phy": 67,
        "chem": 58,
        "math": 49
    }
}

# Add or update a subject
student["subjects"]["eng"] = 74
student["subjects"]["math"] = 55

# Print entire dictionary
print(student)
print(len(student))

# Print keys
print(student.keys())
print(list(student.keys()))

# Print values
print(student.values())
print(list(student.values()))

# Print items (key-value pairs)
print(list(student.items()))

# Access key-value pair (as a tuple)
pair = list(student.items())
print(pair[0])

# Safe way to get value of 'name'
print(student.get("name"))

# Direct access to non-existent key causes error:
# print(student["name1"])  # KeyError

# Safer alternative: get() returns None if key doesn't exist
print(student.get("name1"))

# Update the Dictionary
student.update({"city": "Mumbai", "age": 20})
print(student)
