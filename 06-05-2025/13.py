with open("log.txt", "a+") as f:
    f.write("Appended line.\n")
    f.seek(0)  # Move cursor to the beginning
    print(f.read())
