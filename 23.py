#Write a Python program to find the key that has the highest value in a dictionary, without using `max()`
def highest_value(a):
    highest = list(a.values())[0]
    key_name = list(a.keys())[0]
    for i in a:
        if a[i] > highest:
            highest = a[i]
            key_name = i
    print("Name with highest value =", key_name)
    print("Highest value =", highest)
a = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    a[name] = marks
highest_value(a)