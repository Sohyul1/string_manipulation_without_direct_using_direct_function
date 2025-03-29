# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Sample string
sample_string = "hOW many WORDS are HERE?"

# Create a function to replicate capitalize()
if len(sample_string) > 0:
    new_string = sample_string[0].upper() + sample_string[1:].lower()

# Implement