# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Sample string
sample_string = "hello I am under the water"
total_characters = 30

# Spaces to add 
spaces =  total_characters - len(sample_string)
left_space = spaces // 2
right_space = spaces - left_space

# Create a function to replicate center()
if spaces > 0:
    new_string = " " * left_space + sample_string + " " * right_space
else:
    new_string = sample_string

# Implement
print(new_string)