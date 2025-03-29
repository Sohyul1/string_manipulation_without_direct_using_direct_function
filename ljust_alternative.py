# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Sample string 
sample_string = "hello HAHAHAHAHAHa"
total_characters = 50

# Sapces to add 
spaces = total_characters - len(sample_string)

# Create a function to replicate ljust()
if spaces > 0:
    new_string = " " * abs(spaces) + sample_string
else:
    new_string = sample_string

# Implement it
print(new_string)
