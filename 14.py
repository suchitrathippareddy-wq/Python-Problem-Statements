# palindrome string
def palindrome(a):
    reverse = ""
    for i in a:
        reverse = i + reverse
    if a == reverse:
        return "Palindrome"
    else:
        return "Not Palindrome"
a = input("Enter string: ")
temp = palindrome(a)
print(temp)