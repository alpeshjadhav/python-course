# if
x = 10
if x > 5:
    print("x is greater than 5")

# if-else
age = 21

if (age >= 18):
    print("Can vote and apply for license")
else:
    print("Can not vote")

# if-elif-else
light = "green"

if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
else:
    print("Slow")

# Nested Conditions
age = 20
country = "USA"

if country == "USA":
    if age >= 18:
        print("You are eligible to vote in the USA.")
    else:
        print("You are not old enough to vote in the USA.")
else:
    print("This eligibility check is only for the USA.")
