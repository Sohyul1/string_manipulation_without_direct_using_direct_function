# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Sample string 
smpl_string = "Hi HelLo hoW ArE YOU"

# List of alphabets 
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# New string
new_string = ""

# Create a function to replicate lower()
for char in smpl_string:
    if char in uppercase:
        index = uppercase.index(char)
        new_string += lowercase[index]

    else:
        new_string += char

# Implement
print(new_string)