def count_words(a):
    words = a.split()
    return len(words)

a = input("Enter string: ")

temp = count_words(a)

print("Number of words =", temp)