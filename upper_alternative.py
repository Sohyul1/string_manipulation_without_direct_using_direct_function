# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Sample String
smpl_string = "Hi HelLo hoW ArE YOU"

# List of alphabet 
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# New string
new_string = ""

# Create a function that replicates .upper()
for char in smpl_string:
    if char in lowercase:
        index = lowercase.index(char)
        new_string += uppercase[index]
    else:
        new_string += char

# Implement
print(new_string)