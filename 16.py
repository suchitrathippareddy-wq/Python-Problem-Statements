#Count digits, alphabets, and special characters
def count_characters(a):
    alphabets = 0
    digits = 0
    special = 0
    for i in a:
        if i.isalpha():
            alphabets += 1
        elif i.isdigit():
            digits += 1
        else:
            special += 1
    print("Alphabets =", alphabets)
    print("Digits =", digits)
    print("Special characters =", special)
a = input("Enter string: ")
count_characters(a)