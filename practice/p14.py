# WAP to count the number of students with the “A” grade in the following tuple.
# ("A", "B", "A", "C", "A", "B", "D", "A", "C", "B")
# Store the above values in a list & sort them from “A” to “D”

grades_tuple = ("A", "B", "A", "C", "A", "B", "D", "A", "C", "B")

a_count = grades_tuple.count("A")
print("Number of students with 'A' grade:", a_count)

grades_list = list(grades_tuple)

grades_list.sort()
print("Sorted grades (A to D):", grades_list)
