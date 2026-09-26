#Check palindrome number
def palindrome(a):
    original = a
    reverse = 0
    for i in range(len(str(a))):
        num = a % 10
        reverse = reverse * 10 + num
        a = a // 10
    if original == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
a = int(input("Enter value: "))
temp = palindrome(a)
print(temp)
