# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Sample String
sample_string = " hi IM unDER tHe WaTER"

# Create a function to replicate title()
words_split = sample_string.split()
new_words = []

for word in words_split:
    if len(words_split) > 0:
        changed_words = word[0].upper() + word [1:].lower() 
        new_words.append(changed_words)


# Implement
print(new_words)
