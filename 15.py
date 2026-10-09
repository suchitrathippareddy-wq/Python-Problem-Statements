a = input("Enter string: ")
vowels = 0
consonants = 0
for i in a:
    if i in "aeiou":
        vowels += 1
    else:
        consonants += 1
print("Vowels =", vowels)
print("Consonants =", consonants)