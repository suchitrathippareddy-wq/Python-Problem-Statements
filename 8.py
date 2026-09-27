#Check prime number
def prime_number(a):
    count = 0
    for i in range(1,a + 1):
        if a % i == 0:
            count += 1
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"
a = int(input("Enter value: "))
temp = prime_number(a)
print(temp)