# WAF find the word from file.
# without function
word = "learning"

with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not found!")


# function start
def find_word_in_file(filename, word):
    with open(filename, "r") as f:
        data = f.read()
        if word in data:
            print("Found")
        else:
            print("Not found!")
# function end


# Call the function
find_word_in_file("practice.txt", "learning")
