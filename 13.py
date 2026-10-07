def reverse_string(a):
    reverse = ""
    for i in a:
        reverse = i + reverse
    return reverse
a = input("Enter string: ")
temp = reverse_string(a)
print("Reverse =", temp)