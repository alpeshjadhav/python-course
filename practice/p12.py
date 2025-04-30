# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list = [1, 2, 3, 4, 1, 4]
print("Original list:", list)

copy_list = list.copy()
copy_list.reverse()
print("Reverce list:", copy_list)

if (list == copy_list):
    print("Palindrom")
else:
    print("Non Palindrom")
