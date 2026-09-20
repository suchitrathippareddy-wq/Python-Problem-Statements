#count how many n appears in the tuple
t = tuple(map(int, input("enter n values: ").split()))
n=int(input('enetr one n value:'))
count =0
for i in t:
    if i==n:
        count +=1
print(f'{n} appears {count} times')