# WAF that replace all occurances of java to python in file.
# without function
with open("practice.txt", "r") as f:
    data = f.read()
    print("Original Data:\n", data)

new_data = data.replace("java", "python")
print("Modified Data:\n", new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)


# function start
def replace_java_with_python(filename):
    with open(filename, "r") as f:
        data = f.read()

    new_data = data.replace("java", "python")

    with open(filename, "w") as f:
        f.write(new_data)
# function end


# Call the function
replace_java_with_python("practice.txt")
