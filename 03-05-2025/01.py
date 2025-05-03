# Creating a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}

print(person)
print(type(person))

# Access value by key
print(person["name"])

# Add or update key-value
person["email"] = "alice@xyz.com"
person["surname"] = "Khapra"
print(person)

# Delete a key
del person["age"]
print(person)

# Get keys, values, items
print(person.keys())
print(person.values())
print(person.items())

null_dict = {}
print(null_dict)

null_dict["key1"] = "value1"
print(null_dict)