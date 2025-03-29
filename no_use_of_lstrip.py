# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Sample string
sample_string = "                       Deki iked"

# Create a function to replicate lstrip()
for i in sample_string:
    if i != " ":
        letter_position = sample_string.index(i)
        break

 # Implement 
new_string = sample_string[letter_position:]
print(new_string)