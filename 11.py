# Armstrong number
def armstrong(a):
    orig = a
    total = 0
    for i in range(len(str(a))):
        num = a % 10
        total = total + num ** 3
        a = a // 10
    if orig == total:
        return "Armstrong Number"
    else:
        return "Not Armstrong Number"
a = int(input("Enter value: "))
temp = armstrong(a)
print(temp)