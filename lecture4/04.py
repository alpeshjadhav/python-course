# Empty tuple
t1 = ()
print(t1)
print(type(t1))

# Tuple with elements
t2 = (1, 2, 3)
print(t2)
print(type(t2))

# Tuple without parentheses (not recommended, but valid)
t3 = 4, 5, 6
print(t3)
print(type(t3))

# Single-element tuple (note the comma!)
t4 = (7, )
print(t4)
print(type(t4))

t5 = (t1, t2, t3, t4)
print(t5)
print(type(t5))
