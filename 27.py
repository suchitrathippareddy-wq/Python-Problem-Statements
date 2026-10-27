def above_average(employees):
    total = 0
    for name in employees:
        total += employees[name]
    average = total / len(employees)
    print("Average salary =", average)
    print("Employees earning above average:")
    for name in employees:
        if employees[name] > average:
            print(name, ":", employees[name])
employees = {}
n = int(input("Enter number of employees: "))
for i in range(n):
    name = input("Employee name: ")
    salary = int(input("Salary: "))
    employees[name] = salary
above_average(employees)