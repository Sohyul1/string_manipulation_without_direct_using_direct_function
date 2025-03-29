# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Sample string
sam_string = "   Dek i"

# Create a function to replicate lstrip()
for i in sam_string:
    if i == " ":
        new_string = sam_string.replace(" ", "")

# Implement
print(new_string)