# WAP to print the elements of a list in a single line.
heros = ["salman", "shahruk", "amir", "ajay",
         "sanjay", "anil", "akshay", "jacky", "saif"]


def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(heros)
