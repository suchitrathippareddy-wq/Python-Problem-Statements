#Write a Python program to store student names and their marks in multiple subjects using a nested dictionary. Find the student who scored the highest marks in each subject.

def highest_scorer(students, subjects):
    for subject in subjects:
        highest = -1
        name = ""
        for student in students:
            marks = students[student][subject]
            if marks > highest:
                highest = marks
                name = student
        print("Highest in", subject, "=", name, "(", highest, ")")
students = {}
subjects = ["Maths", "Python"]
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    students[name] = {}
    for subject in subjects:
        marks = int(input("Enter " + subject + " marks: "))
        students[name][subject] = marks
highest_scorer(students, subjects)
