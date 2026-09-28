#Check prime number
def prime_number(a):
    count=0
    for i in range(1,a+1):
        if a % i== 0:
            count +1
    if count==2:
        return "prime"
    else:
        return "not palindrome"
a=int(input("enter value:"))
temp=prime_number(a)
print(temp)