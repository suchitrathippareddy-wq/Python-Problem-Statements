# #program to find the minimum element without using a min() function 
def minimun(a):
    min = a[0]
    for num in a:
        if num<min:
            min=num
    return min

a=list(map(int,input("enter values:").split()))
temp=minimun(a)
print(temp)



#program to read n integer values into alist and find the max and min elements without using a buit-in max() or min() function
def max_min(a):
    max=min=a[0]
    for num in a:
        if num>max:
            max=num
    for num in a:
        if num<min:
            min=num
    return max,min
a=list(map(int,input("enter values:").split()))
max,min=max_min(a)
print("Maximum =", max)
print("Minimum =", min)
