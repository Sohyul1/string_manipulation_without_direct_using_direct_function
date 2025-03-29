# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Sample string 
smpl_string = "Hi HelLo hoW ArE YOU"

# List of alphabets 
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

# Create a function to replicate lower()
for i in smpl_string:
    if i in uppercase:
        index = uppercase.index(i)

# Implement