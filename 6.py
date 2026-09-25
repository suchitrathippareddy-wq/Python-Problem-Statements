#Reverse a number
def reverse_number(a):
    reverse = 0
    for  i in range(len(str(a))):
        num = a % 10 # get the last digit.
        reverse = reverse * 10 + num
        a = a//10 #it removes last digit
    return reverse
a=int(input("enter values:"))
temp=reverse_number(a)
print(temp)