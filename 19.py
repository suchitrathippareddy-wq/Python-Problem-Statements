def replace_spaces(a):
    result = ""
    for i in a:
        if i == " ":
            result = result + "-"   
        else:
            result = result + i 
    return result
a = input("Enter string: ")
temp = replace_spaces(a)
print(temp)

