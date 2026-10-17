#Converting two lists into a dictionary
def convert_dictionary(keys, values):
    result = {}
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result
keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
temp = convert_dictionary(keys, values)
print(temp)