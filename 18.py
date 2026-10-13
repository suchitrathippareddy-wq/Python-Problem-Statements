# Write a Python program to reverse a string without using slicing ([::-1]).


# Take a string as input
s = input("Enter a string: ")

# Initialize an empty string
rev = ""

# Traverse each character in the string
for i in s:
    # Add the current character to the beginning of rev
    rev = i + rev

# Print the reversed string
print("Reversed string:", rev)


# Input
# Enter a string: suchireddy


# Output
# Reversed string: ydderihcus