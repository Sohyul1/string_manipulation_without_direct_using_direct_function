# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Sample String
sample_string = "HeLlO, i'M uNdEr ThE wAtEr 123"
new_string = ""

# Create a function to replicate swapcase()
for char in sample_string:
    if char.islower():
        new_string += char.upper()
    elif char.isupper():
        new_string += char.lower()
    else:
        new_string += char

# Implement
print(new_string)