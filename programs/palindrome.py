a = input("enter a word here: ")
a = a.lower()

rev = a[::-1]

if a == rev:
    print("Palindrome")
else:
    print("Not a palindrome")
