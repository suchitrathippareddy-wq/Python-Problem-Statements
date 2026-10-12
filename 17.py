#Find duplicate characters
def duplicate_characters(a):
    for i in a:
        if a.count(i) > 1:
            print(i)
            a = a.replace(i, "", 1)
a = input("Enter string: ")
duplicate_characters(a)

