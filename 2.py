#Find the largest element in a tuple without using the max() function.

def largest(t):
    largest=t[0]
    for i in t:
        if i > largest:
            largest=i
    return largest
t=tuple(map(int,input('enter n values:').split()))

temp=largest(t)
print(temp)