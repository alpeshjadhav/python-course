# waf to find in which line of the file does the word "learning" occur first.

def find_line_with_word(filename, word):
    with open(filename, "r") as f:
        for line_number, line in enumerate(f, start=1):
            if word in line:
                print(f'Word "{word}" found on line {line_number}')
                return
        print(f'Word "{word}" not found in the file.')


# Call the function
find_line_with_word("practice.txt", "learning")


def check_for_line(filename, word):
    data = True
    line_no = 1
    with open(filename, "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(f'Word "{word}" found on line {line_no}')
                return
            line_no += 1


check_for_line("practice.txt", "learning")
