def merge_dicts(a, b):
    result = a.copy()
    for key in b:
        if key in result:
            result[key] += b[key]
        else:
            result[key] = b[key]
    return result
a = {}
b = {}
n = int(input("Enter number of entries in first dictionary: "))
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    a[key] = value
m = int(input("Enter number of entries in second dictionary: "))
for i in range(m):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    b[key] = value
temp = merge_dicts(a, b)
print("Merged dictionary =", temp)

