# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# Sample String
sample_string = "hello HAHAHAHAHAH"
total_characters = 50

# Spaces to add 
spaces = total_characters - len(sample_string)

# Create a function the replicates rjust()
if spaces > 0:
    new_string = " " * spaces + sample_string
else:
    new_string = sample_string

# Implement
print(new_string)