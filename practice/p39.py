# from a file containing numbers separated by comma print the  count of even numbers

# without function
count = 0
with open("numbers.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count += 1

print(count)


def count_even_numbers(filename):
    with open(filename, "r") as f:
        data = f.read()
        numbers = [int(num.strip()) for num in data.split(",")]
        even_count = sum(1 for num in numbers if num % 2 == 0)
        print(f"Count of even numbers: {even_count}")


# Call the function
count_even_numbers("numbers.txt")
