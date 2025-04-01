# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Sample string
sample_string = "Deki iked      "

# Create a function to replicate rstrip()
for i in reversed(sample_string):
    if i != " ":
        letter_position = sample_string.rindex(i)
        break

# Implement 
new_string = sample_string[:letter_position + 1]
print(new_string)