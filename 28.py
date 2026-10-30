def first_non_repeating(numbers):
    frequency = {}
    # Count frequency of each element
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    # Find first non-repeating element
    for num in numbers:
        if frequency[num] == 1:
            return num
    return None
numbers = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)
result = first_non_repeating(numbers)
if result is not None:
    print("First non-repeating element =", result)
else:
    print("No non-repeating element found")